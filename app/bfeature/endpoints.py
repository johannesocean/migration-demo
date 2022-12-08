"""
Created on 2022-12-08 15:25
@author: johannes
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.bfeature import crud
from app.core.db.database import get_db
from app.bfeature.schema import BSchema, BBase

router = APIRouter(
    prefix="/bfeature",
    tags=["bfeature"],
)


@router.get("/", response_model=list[BSchema])
def read_b(b_number: int, db: Session = Depends(get_db)):
    b = crud.get_b(db, b_number)
    return b


@router.post("/", response_model=BSchema)
def create_b(b: BBase, db: Session = Depends(get_db)):
    extracted_b = crud.create_b_extracted(db=db, b=b)
    return extracted_b
