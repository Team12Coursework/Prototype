import os
import secrets
from typing import Tuple

import dotenv

# load the .env file to get the postgres uri
dotenv.load_dotenv()


class Config:
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = 'HS256'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = os.getenv('TESTING_DATABASE_URI')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = os.getenv('PRODUCTION_DATABASE_URI')


# global object pattern will create the correct config at import time
if os.getenv('DEBUG') == '1':
    config: Config = TestingConfig()
else:
    config: Config = ProductionConfig()
