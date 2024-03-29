import json

from fastapi import WebSocket

from .game_manager import GameManager
from .. import schemas


class RoomFull(Exception):
    """Exception raised if the room is full"""


class ConnectionManager:
    """ConnectionManager class used to handle active WebSocket connections"""
    def __init__(self) -> None:
        self.connected: dict[str, GameManager] = {}

    async def join_game(self, room_id: str, player: schemas.Player) -> None:
        """method to create a room on player join game"""
        if not self.connected.get(room_id):
            self.connected[room_id] = GameManager(room_id)
        self.connected[room_id].add_player(player)

    async def _emit_player_disconnect(self, room: str, player: schemas.Player) -> None:
        msg: str = json.dumps({
            'type': 'playerDisconnect',
            'player': player.dict(exclude={'socket'}),
        })
        await self.broadcast(room, msg)

    async def disconnect(self, room: str, socket: WebSocket) -> None:
        """method to remove player from connections"""
        _room = self.connected[room]
        for i, player in enumerate(_room.players):
            if player.socket == socket:
                _room.forfeit(i)
                break

    async def send_personal_message(self, message: str, websocket: WebSocket) -> None:
        """method to send a message to a specific connection"""
        await websocket.send_text(message)

    async def broadcast(self, room: str, message: str) -> None:
        """method to send a message to an entire room"""
        for player in self.connected[room].players:
            await player.socket.send_text(message)


manager = ConnectionManager()