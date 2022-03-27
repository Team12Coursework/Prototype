import os
import secrets

class Config:
    SECRET_KEY = secrets.token_urlsafe(32)
    ALGORITHM = 'HS256'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

config = Config()
