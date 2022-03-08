from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Integer, ForeignKey, Column, String

Base = declarative_base()


class Theme(Base):
    """class to represent theme table in the database."""

    __tablename__: str = 'themes_tab'

    id          = Column(Integer, primary_key=True, index=True)
    dictionary  = Column(Integer) # needs editing
    description = Column(String)


class DictionaryMapping(Base):
    """class to represent the dictionary_mapping table in the database,
    the dictionary_mapping represents the many-to-many link between
    themes and words."""

    __tablename__: str = 'dictionary_mapping_tab'

    @declared_attr
    def word_id(cls) -> Column:
        return Column(String, ForeignKey('words_tab.word'), primary_key=True)

    @declared_attr
    def theme_id(cls) -> Column:
        return Column(Integer, ForeignKey('themes_tab.id'), primary_key=True)


class User(Base):
    """class representing a user in the database"""

    __tablename__ = 'users_tab'

    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    email    = Column(String, unique=True, index=True)


class Words(Base):
    __tablename__ = 'words_tab'

    word       = Column(String, primary_key=True, index=True)
    definition = Column(String)