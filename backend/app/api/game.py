import datetime
import json
from typing import Dict

from app import schemas
from app.api.connection_manager import ConnectionManager
from app.api.game_manager import GameManager
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websockets.exceptions import ConnectionClosedOK


router = APIRouter()
connection_manager = ConnectionManager()
game_manager = GameManager()


"""file holds all of the routes for the game behaviour."""


def filter_message(data: Dict[str, str]) -> Dict[str, str]:
    """function to filter chat messages"""

    return json.dumps(data)


async def process_next_turn() -> None:
    # there are two possible types for the next turn event.
    # wordPlaced, and turnSkipped. A turnSkipped event can be raised for a multitude of reasons,
    # the outcome is the same, the turn will be skipped, no points will be awarded.

    # incoming data should be in the format:
    # {
    #    'type': 'wordPlaced',
    #    'newBoard': List[List[str]], # 15 x 15 board
    # }

    data = json.dumps({

    })


async def process_game_start(room) -> None:
    """function to process the game start"""

    data = json.dumps({
        'type': 'gameStart',
        'tiles': [
            ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        ],
        'sentAt': datetime.datetime.now().time(),
        # the first player to join the lobby is always the first to start the game, can change later if necessary.
        'playersTurn': connection_manager.connected[room][0].name,
    })
    await connection_manager.broadcast(room, data)


async def process_room_join(websocket, decoded, room) -> None:
    """function to process a player joining the room"""

    # incoming data should be in the format:
    # {
    #   'type': 'playerJoin',
    #   'player': {
    #       'name': str,
    #   },
    #   'sentAt': datetime.date,
    # }

    player = schemas.Player.parse_obj(decoded['player'])
    print(f'player {player} joined room {room}')

    # outgoing data should be in the format:
    # the first player to enter the lobby will be the lobby owner
    # and will have the first turn.
    data = json.dumps({
        'type':         'playerJoin',
        'players':      [player.name for player in connection_manager.connected[room]],
        'sentAt':       datetime.datetime.now().time(),
    })

    await connection_manager.join(room, player, websocket)
    await connection_manager.broadcast(room, data)

    if len(connection_manager.connected[room]) == 2:
        await process_game_start(room)


@router.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room: str):
    """method to handle WebSocket events from frontend"""
    await connection_manager.connect(websocket)
    try:
        while True:
            data: str = await websocket.receive_text()
            decoded = json.loads(data)
            if decoded['type'] == 'playerJoin':
                await process_room_join(websocket, decoded, room)
            elif decoded['type'] == 'message':
                msg = filter_message(decoded)
                print(f'received message: {msg}')
                await connection_manager.broadcast(room, msg)
            else:
                await connection_manager.broadcast(room, data)
    except (WebSocketDisconnect, ConnectionClosedOK):
        await connection_manager.disconnect(room, websocket)
        await connection_manager.broadcast(room, json.dumps({'type': 'playerLeft'}))
        print(f'player disconnected')