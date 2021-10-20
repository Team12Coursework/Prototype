import secrets
from typing import Tuple

class Config:
    SECRET_KEY: str = secrets.token_urlsafe(32)

    POSTGRES_HOST: str = 'localhost'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = 'character_connect'

    # this definitely needs to be changed to use
    # an .env file
    POSTGRES_PASSWORD: str = 'postgres'

    SQLALCHEMY_DATABASE_URI: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

config: Config = Config()