from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Integer, ForeignKey

from .base import Base

class DictionaryMapping(Base):
    """
    class to represent the dictionary_mapping table in the database,
    the dictionary_mapping represents the many-to-many link between
    themes and words.
    """

    @declared_attr
    def word_id(cls) -> Column:
        return Column(String, ForeignKey('words_tab.id'), primary_key=True)

    @declared_attr
    def dictionary_id(cls) -> Column:
        return Column(Integer, ForeignKey('dictionary_tab.id'), primary_key=True)
