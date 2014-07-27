from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
	"""
	Performs database connection using database settings from settings.py.
	Returns sqlalchemy engine instance
	"""
	return create_engine(URL(**settings.DATABASE))

def create_job_post_table(engine):
	DeclarativeBase.metadata.create_all(engine)

def create_keyword_table(engine):
	DeclarativeBase.metadata.create_all(engine)

def create_job_keyword_table(engine):
	DeclarativeBase.metadata.create_all(engine)

class JobPost(DeclarativeBase):
	""" SqlAlchemy JobPost model """
	__tablename__ = "jobPost"

	title = Column('title', VARCHAR(50))
	posted = Column('posted', VARCHAR(15))
	original_post_link = Column('original_post_link', VARCHAR(50))
	location = Column('location', VARCHAR(50), nullable=True)
	job_title = Column('job_title', VARCHAR(50), nullable=True)
	address = Column('address', VARCHAR(50), nullable=True)
	map_link = Column('map_link', VARCHAR(50), nullable=True)
	compensation = Column('compensation', VARCHAR(50), nullable=True)
	text = Column('text', VARCHAR(500))
	_id = Column(Integer, primary_key=True)

class Keyword(DeclarativeBase):
	""" SqlAlchemy Keyword model """
	__tablename__ = 'keyword'

	word = Column('word', VARCHAR(50))
	_id = Column(Integer, primary_key=True)

class JobKeyword(DeclarativeBase):
	""" SqlAlchemy JobKeyword model """
	__tablename__ = 'jobKeyword'

	word_id = Column(Integer, foreign_key=True)
	post_id = Column(Integer, foreign_key=True)

