"""
Created on 2022-12-08 15:34
@author: johannes
"""
from datetime import datetime
from typing import Optional
from app.core.db.database import AppBaseModel


class MoonBase(AppBaseModel):
    moon_number: Optional[int]


class MoonSchema(MoonBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
