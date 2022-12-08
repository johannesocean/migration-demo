"""
Created on 2022-12-08 15:25
@author: johannes
"""
from fastapi import APIRouter

router = APIRouter(
    prefix="/bfeature",
    tags=["bfeature"],
)
