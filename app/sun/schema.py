"""
Created on 2022-12-08 15:34
@author: johannes
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class SunBase(BaseModel):
    sun_number: int


class SunSchema(SunBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
