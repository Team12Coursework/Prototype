from sqlalchemy.orm import Session

from app.core.config import config
from app.models.base import Base
from app.models import *
from app.database.session import engine

def init_db(database: Session) -> None:
    Base.metadata.create_all(bind=engine)