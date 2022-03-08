from sqlalchemy.orm.session import Session

from ..database.session import SessionLocal

"""
file holds all of the API dependancies
which can be injected into the routes using the FastAPI
dependancy injection pattern
"""

def get_database() -> Session:
    """function used to inject a database connection into routes"""
    database: Session = SessionLocal()
    try:
        yield database
    finally:
        database.close()
