from fastapi import APIRouter

from app.api import game
from app.api import user
from app.api import chat

router = APIRouter()

router.include_router(
    game.router,
    prefix='/game',
)

router.include_router(
    user.router,
    prefix='/user',
)

router.include_router(
  chat.router,
  prefix="/chat",
)