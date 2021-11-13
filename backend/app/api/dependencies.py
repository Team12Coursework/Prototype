from sqlalchemy.orm.session import Session

from app.database.session import SessionLocal

def get_database() -> Session:
    """function used to inject a database connection into routes"""
    database: Session = SessionLocal()
    try:
        yield database
    finally:
        database.close()