"""
Created on 2022-12-08 15:34
@author: johannes
"""
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.db.association_tables import ab_table
from app.core.db.database import Base


class AModel(Base):
    __tablename__ = "a"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    number = Column(Integer, nullable=True)

    b = relationship(
        "BModel", secondary=ab_table, back_populates="a"
    )
