from sqlalchemy.orm import Session

from ..models import *
from .session import engine

def init_db(database: Session) -> None:
    """
    function invokes SQLAlchemy create_all which will create the database tables if they do not exist,
    this is especially useful for testing as an empty Docker container can be populated with the correct tables.
    """
    Base.metadata.create_all(bind=engine)
