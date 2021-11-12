from sqlalchemy import Integer, String, Column

from .base import Base

class Theme(Base):
    """
    class to represent theme table in the database.
    """

    __tablename__: str = 'themes_tab'

    id: Column = Column(Integer, primary_key=True, index=True)
    dictionary: Column(Integer) # needs editing
    description: Column = Column(String)
