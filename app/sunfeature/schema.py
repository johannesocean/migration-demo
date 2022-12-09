"""
Created on 2022-12-08 15:34
@author: johannes
"""
from datetime import datetime
from typing import Optional
from app.core.db.base import AppBaseModel


class SunBase(AppBaseModel):
    sun_number: Optional[int]


class SunSchema(SunBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
