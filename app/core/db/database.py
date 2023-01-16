"""
Created on 2022-12-08 15:29
@author: johannes
"""
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine: Engine = create_engine(
    settings.DB_CONNECTION_STRING,
    # connect_args={"check_same_thread": False},  # only for sqlite
    echo=True  # nice for testing
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> object:
    """Database dependencies."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
