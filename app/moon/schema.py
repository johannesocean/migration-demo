"""
Created on 2022-12-08 15:34
@author: johannes
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class MoonBase(BaseModel):
    moon_number: int


class MoonSchema(MoonBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
