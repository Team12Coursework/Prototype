import datetime
import json
from typing import Callable, Dict, List, Optional, Any

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError

from .connection_manager import ConnectionManager
from .game_manager import GameManager, Player, InvalidWordException


router = APIRouter()
connection_manager = ConnectionManager()


"""file holds all of the routes for the game behaviour."""


def current_time() -> str:
    return datetime.datetime.now().strftime('%H:%M:%S')

async def handle_perk_error(callback: Callable[Any, Any], connection_manager, websocket, *args) -> None:
    try:
        callback(*args)
    except ValueError as error:
        await connection_manager.send_personal_message(json.dumps({"type": "gameError", "message": str(error)}), websocket)


def filter_message(data: Dict[str, str]) -> Dict[str, str]:
    """function to filter chat messages"""
    
    bannedWords = ["shit","fuck","crap","bitch"] # will add more words to this
    
    chatMessage = data.get('message')
    censoredMessageList = []
    
    for word in chatMessage.split():
        if word in bannedWords:
            censoredMessageList.append("[redacted]")
        else:
         censoredMessageList.append(word)
    
    censoredMessage = " ".join(censoredMessageList)
    data.update({'message': censoredMessage})
    return json.dumps(data)


def process_next_turn(room_id: str, board: List[List[Optional[str]]]) -> Dict[str, str]:
    """process the next turn, this function doesn't return anything to the client"""
    game: GameManager = connection_manager.connected[room_id]
    try:
        game.next_turn(board)
        return game.asdict()
    except InvalidWordException as error:
        print(error)
        return {'type': 'updateError', 'message': 'invalid word placed'}


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
            elif decoded['type'] == 'gameUpdate':
                state: Dict[str, str] = process_next_turn(room, decoded['board'])
                print(decoded, state)
                if state['type'] == 'gameUpdate':
                    await connection_manager.broadcast(room, json.dumps(state))
                elif state['type'] == 'updateError':
                    await connection_manager.send_personal_message(json.dumps(state), websocket)
            elif decoded['type'] == "perkActive":
                    game: GameManager = connection_manager.connected[room]
                    if decoded['subtype'] == 'oneRandomLetter':
                        await handle_perk_error(game.extra_letter_perk, connection_manager, websocket, 1)
                    elif decoded['subtype'] == 'twoRandomLetters':
                        await handle_perk_error(game.extra_letter_perk, connection_manager, websocket, 2)
                    elif decoded['subtype'] == 'changeLetters':
                        game.change_letters_perk()
                    await connection_manager.send_personal_message(game.asdict(), websocket)
    except (WebSocketDisconnect, ConnectionClosedOK, ConnectionClosedError):
        await connection_manager.disconnect(room, websocket)
        await connection_manager.broadcast(room, json.dumps({'type': 'playerLeft'}))
        print(f'player disconnected')