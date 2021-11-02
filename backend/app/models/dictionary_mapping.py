from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Integer, ForeignKey, Column, String

from .base import Base

class DictionaryMapping(Base):
    """
    class to represent the dictionary_mapping table in the database,
    the dictionary_mapping represents the many-to-many link between
    themes and words.
    """

    __tablename__: str = 'dictionary_mapping_tab'

    @declared_attr
    def word_id(cls) -> Column:
        return Column(String, ForeignKey('words_tab.word'), primary_key=True)

    @declared_attr
    def theme_id(cls) -> Column:
        return Column(Integer, ForeignKey('themes_tab.id'), primary_key=True)
