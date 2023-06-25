from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from datetime import datetime

engine = create_engine('sqlite:///db.sqlite3')
Base   = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    name = Column(String)
    joined_at = Column(DateTime, default=datetime.now())


Base.metadata.create_all(engine)