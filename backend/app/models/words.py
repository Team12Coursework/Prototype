from sqlalchemy import String, Column

from .base import Base

class Words(Base):
    __tablename__: str = 'words_tab'

    word: Column = Column(String, primary_key=True, index=True)
    definition: Column = Column(String)
