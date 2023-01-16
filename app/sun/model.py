"""
Created on 2022-12-08 15:34
@author: johannes
"""
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.db.association_tables import sunmoon_table
from app.core.db.database import Base


class SunModel(Base):
    __tablename__ = "sun"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    sun_number = Column(Integer, nullable=True)

    moon = relationship(
        "MoonModel", secondary=sunmoon_table, back_populates="sun"
    )
