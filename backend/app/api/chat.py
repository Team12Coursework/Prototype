from fastapi import APIRouter
from fastapi import FastAPI, WebSocket

router = APIRouter()

@router.websocket("/ws/{client_id}")
def accept(websocket:WebSocket):
    print("New connection establishing....")
    websocket.accept
    print("New connection established!")
    while websocket.accept == True:
          accept.msg = websocket.receive()


@router.websocket("/ws/{client_id}")
def broadcast (websocket:WebSocket):
    websocket.send(accept.msg)



        
