"""
Created on 2022-12-08 15:34
@author: johannes
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BBase(BaseModel):
    number: Optional[float]


class BSchema(BBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
