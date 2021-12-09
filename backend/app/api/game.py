import datetime
import json
from typing import Dict

from app import schemas
from app.api.connection_manager import ConnectionManager
from app.api.game_manager import GameManager, Player
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError
import numpy as np


router = APIRouter()
connection_manager = ConnectionManager()


"""file holds all of the routes for the game behaviour."""

def current_time() -> str:
    return datetime.datetime.now().strftime('%H:%M:%S')

def filter_message(data: Dict[str, str]) -> Dict[str, str]:
    """function to filter chat messages"""

    return json.dumps(data)

def process_next_turn(room_id: str, board: np.ndarray) -> Dict[str, str]:
    """process the next turn, this function doesn't return anything to the client"""
    game: GameManager = connection_manager.connected[room_id].game
    game.next_turn(board)
    return game.asdict()

async def process_room_join(websocket, decoded, room_id: str) -> None:
    """function to process a player joining the room"""
    name = decoded['player']
    player = Player(name, websocket)

    print(f'player {player} joined room {room_id}')

    await connection_manager.join_game(room_id, player)
    game = connection_manager.connected[room_id]

    if game.full:
        game.reset()
    await connection_manager.broadcast(room_id, json.dumps(game.asdict()))


@router.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room: str):
    """method to handle WebSocket events from frontend"""
    await websocket.accept()
    try:
        while True:
            data: str = await websocket.receive_text()
            decoded = json.loads(data)
            if decoded['type'] == 'playerJoin':
                await process_room_join(websocket, decoded, room)
            elif decoded['type'] == 'message':
                msg = filter_message(decoded)
                await connection_manager.broadcast(room, msg)
    except (WebSocketDisconnect, ConnectionClosedOK, ConnectionClosedError):
        await connection_manager.disconnect(room, websocket)
        await connection_manager.broadcast(room, json.dumps({'type': 'playerLeft'}))
        print(f'player disconnected')