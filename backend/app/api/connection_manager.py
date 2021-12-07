import dataclasses
import json
from typing import List, Dict

from fastapi import WebSocket

from app import schemas


@dataclasses.dataclass
class Player:
    """dataclass to hold some attributes about each player in the lobby"""
    name: str
    socket: WebSocket

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f'Player(name={self.name})'


class ConnectionManager:
    """ConnectionManager class used to handle active WebSocket connections"""
    def __init__(self) -> None:
        self.connected: Dict[str, List[Player]] = {}

    async def connect(self, websocket: WebSocket) -> None:
        """method to accept an incoming WebSocket connection"""
        await websocket.accept()

    async def join(self, room: str, player: schemas.Player, websocket: WebSocket) -> None:
        """method to move the player from staging to an active room on successful connect"""
        if not self.connected.get(room):
            self.connected[room] = []
        player.socket = websocket
        self.connected[room].append(player)

    async def _emit_player_disconnect(self, room: str, player: schemas.Player) -> None:
        msg: str = json.dumps({
            'type': 'playerDisconnect',
            'player': player.dict(exclude={'socket'}),
        })
        await self.broadcast(room, msg)

    async def disconnect(self, room: str, socket: WebSocket) -> None:
        """method to remove player from connections"""
        for i, player in enumerate(self.connected[room]):
            if player.socket == socket:
                player = self.connected[room].pop(i)
                break
        await self._emit_player_disconnect(room, player)

    async def send_personal_message(self, message: str, websocket: WebSocket) -> None:
        """method to send a message to a specific connection"""
        await websocket.send_text(message)

    async def broadcast(self, room: str, message: str) -> None:
        """method to send a message to an entire room"""
        for player in self.connected[room]:
            await player.socket.send_text(message)


manager = ConnectionManager()