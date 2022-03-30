import datetime
import json
from typing import Callable, Dict, List, Optional, Any
import logging

from fastapi import APIRouter, WebSocket, Depends
from starlette.websockets import WebSocketDisconnect
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError
from jose import JWTError, jwt
from functools import lru_cache

from .connection_manager import ConnectionManager
from .dependencies import get_database
from .game_manager import GameManager, Player, InvalidWordException
from ..core.config import config
from ..models import User, DictionaryMapping


router = APIRouter()
connection_manager = ConnectionManager()


"""file holds all of the routes for the game behaviour."""


def current_time() -> str:
    return datetime.datetime.now().strftime('%H:%M:%S')

def token_valid(token: str, database) -> bool:
    """function to check if the given JWT token is valid
    1) check that the token decodes correctly
    2) check that the decoded token contains data
    3) check that the contained data is valid
        3.1) check that the given username is valid
        3.2) check that the given token isn't expired
    """
    logger = logging.getLogger("uvicorn.token_valid")
    # 1) check if the token is a valid JWT token
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
    except JWTError:
        logger.warning("JWT decode error")
        return False

    # 2) check if the token contains a username
    username: str | None = payload.get('sub')
    if username is None:
        logger.warning("JWT username is None")
        return False

    # 3.2) check the token is expired, this check is done before the database query
    # as if this fails, it avoids the overhead of making a database call.
    exp = payload.get("exp")
    if exp is None:
        logger.warning("JWT exp is None")
        return False
    if datetime.datetime.fromtimestamp(exp) < datetime.datetime.utcnow():
        logger.warning("JWT is expired")
        return False

    # 3.1) check if the token contains a valid username
    user = database.query(User).where(username == User.username).first()
    if user is None:
        logger.warning("JWT user does not exist in database")
        return False
    logger.info("valid JWT received")
    return True

async def handle_perk_error(callback: Callable[Any, Any], connection_manager, websocket, *args) -> None:
    try:
        callback(*args)
    except Exception as error:
        print("exception raised in perk error")
        await connection_manager.send_personal_message(json.dumps({"type": "updateError", "message": str(error)}), websocket)


def filter_message(data: Dict[str, str], database) -> Dict[str, str]:
    """function to filter chat messages"""
    banned_words = get_wordset(database, 2)

    chatMessage = data.get('message')
    censoredMessageList = []

    for word in chatMessage.split():
        if word.lower() in banned_words:
            censoredMessageList.append("****")
        else:
            censoredMessageList.append(word)

    censoredMessage = " ".join(censoredMessageList)
    data.update({'message': censoredMessage})
    return json.dumps(data)

@lru_cache
def get_wordset(database, wordset: int) -> list[str]:
    words = database.query(DictionaryMapping.word).where(DictionaryMapping.theme_id == wordset).all()
    return [w[0] for w in words]

def process_next_turn(room_id: str, board: List[List[Optional[str]]], database) -> Dict[str, str]:
    """process the next turn, this function doesn't return anything to the client"""
    game: GameManager = connection_manager.connected[room_id]
    words = get_wordset(database, game.wordset)

    try:
        game.next_turn(board, words)
        return game.asdict()
    except InvalidWordException as error:
        return {'type': 'updateError', 'message': 'invalid word placed'}


async def process_room_join(websocket, decoded, room_id: str, database) -> None:
    """function to process a player joining the room"""
    # TODO: this will cause an issue with the game start. If this player gets
    # removed from the game, the game still won't be able to start. This isn't
    # pressing.
    print("recieved process_room_join event", decoded)
    if not token_valid(decoded["token"], database):
        await connection_manager.send_personal_message(
            json.dumps({"type": "authError", "msg": "The given token is invalid, you will be disconnected from the game"}),
            websocket)
        await websocket.close()
        return

    name = decoded['player']
    player = Player(name, websocket)

    print(f'player {player} joined room {room_id}')

    await connection_manager.join_game(room_id, player)
    game = connection_manager.connected[room_id]

    if game.full:
        game.reset()
    await connection_manager.broadcast(room_id, json.dumps(game.asdict()))


@router.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room: str, database = Depends(get_database)):
    """method to handle WebSocket events from frontend"""
    await websocket.accept()
    try:
        while True:
            data: str = await websocket.receive_text()
            decoded = json.loads(data)
            if decoded['type'] == 'playerJoin':
                await process_room_join(websocket, decoded, room, database)
            elif decoded['type'] == 'message':
                msg = filter_message(decoded, database)
                await connection_manager.broadcast(room, msg)
            elif decoded['type'] == 'gameUpdate':
                state: Dict[str, str] = process_next_turn(room, decoded['board'], database)
                if state['type'] == 'gameUpdate':
                    await connection_manager.broadcast(room, json.dumps(state))
                elif state['type'] == 'updateError':
                    await connection_manager.send_personal_message(json.dumps(state), websocket)
            elif decoded['type'] == "activatePerk":
                    game = connection_manager.connected[room]
                    if decoded['subtype'] == 'oneRandomLetter':
                        await handle_perk_error(game.extra_letter_perk, connection_manager, websocket, 1)
                    elif decoded['subtype'] == 'twoRandomLetters':
                        await handle_perk_error(game.extra_letter_perk, connection_manager, websocket, 2)
                    elif decoded['subtype'] == 'changeLetters':
                        await handle_perk_error(game.change_letters_perk, connection_manager, websocket)
                    print("perk activated, new game state", game.asdict())
                    await connection_manager.send_personal_message(json.dumps(game.asdict()), websocket)
    except (WebSocketDisconnect, ConnectionClosedOK, ConnectionClosedError):
        _room = connection_manager.connected[room]
        print("disconnect raised in room", room)
        await connection_manager.disconnect(room, websocket)
        print(f'player disconnected')
        await connection_manager.broadcast(room, json.dumps(_room.asdict()))
    except AssertionError:
        print("player forcefully disconnected")