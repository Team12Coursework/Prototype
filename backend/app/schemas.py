from typing import Optional

from pydantic import BaseModel
from fastapi import WebSocket

"""
Pydantic models representing different pieces of data that are used throughout
the project. Pydantic allows data validation and will automatically convert between
JSON types from the frontend and Python types required for the backend/ Database.
"""


class User(BaseModel):
    username: str
    password: str


class Player(BaseModel):
    name: str
    socket: Optional[WebSocket] = None

    class Config:
        arbitrary_types_allowed = True