from app.database.init_db import init_db
from app.database.session import SessionLocal

def init() -> None:
    database = SessionLocal()
    init_db(database)

if __name__ == '__main__':
    init()