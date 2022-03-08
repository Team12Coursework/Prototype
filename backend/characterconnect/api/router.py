from fastapi import APIRouter

from . import game, user

router = APIRouter()

"""
import all of the subrouters from the different API files
"""

router.include_router(
    game.router,
    prefix='/game',
)

router.include_router(
    user.router,
    prefix='/user',
)
