"""
Created on 2022-12-08 15:29
@author: johannes
"""
from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey, Table

from app.core.db.database import Base


class ABModel(Base):
    __tablename__ = "a_b"

    a_id = Column(Integer, primary_key=True)
    b_id = Column(Integer, primary_key=True)


ab_table = Table(
    "a_b",
    Base.metadata,
    Column("a_id", ForeignKey("a.id"), primary_key=True),
    Column("b_id", ForeignKey("b.id"), primary_key=True),
    extend_existing=True
)
