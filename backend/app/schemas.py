from pydantic import BaseModel

"""
Pydantic models representing different pieces of data that are used throughout
the project. Pydantic allows data validation and will automatically convert between
JSON types from the frontend and Python types required for the backend/ Database.
"""

class User(BaseModel):
    username: str
    password: str
