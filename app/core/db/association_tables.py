"""
Created on 2022-12-08 15:29
@author: johannes
"""
from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey, Table

from app.core.db.database import Base


class SunMoonModel(Base):
    __tablename__: str = "sun_moon"

    sun_id: int = Column(Integer, primary_key=True)
    moon_id: int = Column(Integer, primary_key=True)


sunmoon_table = Table(
    "sun_moon",
    Base.metadata,
    Column("sun_id", ForeignKey("sun.id"), primary_key=True),
    Column("moon_id", ForeignKey("moon.id"), primary_key=True),
    extend_existing=True
)
