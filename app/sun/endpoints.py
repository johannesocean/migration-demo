"""
Created on 2022-12-08 15:25
@author: johannes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.sun import crud
from app.sun.schema import SunSchema, SunBase
from app.core.db.database import get_db


router = APIRouter(
    prefix="/sun",
    tags=["sun"],
)


@router.get("/", response_model=list[SunSchema])
def read_sun(sun_number: int, db: Session = Depends(get_db)):
    sun = crud.get_sun(db, sun_number)
    return sun


@router.post("/", response_model=SunBase)
def create_sun(sun: SunBase, db: Session = Depends(get_db)):
    extracted_sun = crud.create_sun_extracted(db=db, sun=sun)
    return extracted_sun
