"""
Created on 2022-12-08 15:34
@author: johannes
"""
from sqlalchemy.orm import Session

from app.moonfeature.model import MoonModel
from app.moonfeature.schema import MoonBase


def get_moon(db: Session, moon_number: int):
    return db.query(MoonModel).filter(MoonModel.number == moon_number).first()


def upsert_moon(db: Session, moon: MoonBase):
    db_moon = get_moon(db=db, moon_number=moon.moon_number)
    if db_moon:
        return db_moon
    else:
        try:
            db_moon = MoonModel(**moon.dict())
            db.add(db_moon)
            db.commit()
            db.refresh(db_moon)
            return db_moon
        except Exception as e:
            raise e
