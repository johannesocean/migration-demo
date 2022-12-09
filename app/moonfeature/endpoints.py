"""
Created on 2022-12-08 15:25
@author: johannes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.moonfeature import crud
from app.core.db.database import get_db
from app.moonfeature.schema import MoonSchema, MoonBase

router = APIRouter(
    prefix="/moonfeature",
    tags=["moonfeature"],
)


@router.get("/", response_model=list[MoonSchema])
def read_moon(moon_number: int, db: Session = Depends(get_db)):
    moon = crud.get_moon(db, moon_number)
    return moon


@router.post("/", response_model=MoonSchema)
def create_moon(moon: MoonBase, db: Session = Depends(get_db)):
    extracted_moon = crud.create_moon_extracted(db=db, moon=moon)
    return extracted_moon
