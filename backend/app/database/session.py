from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True
)

# sessionmaker creates a class SessionLocal
# which can then be instantiated
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)