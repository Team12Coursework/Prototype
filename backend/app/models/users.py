from .base import Base

class User(Base):
    """
    class representing a user in the database
    """

    __tablename__: str = 'users_tab'

    id: Column = Column(Integer, primary_key=True, index=True)
    username: Column = Column(String(255), unique=True, index=True)
    password: Column = Column(String(255))
    email: Column = Column(String, unique=True, index=True)
