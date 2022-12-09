"""
Created on 2022-12-08 15:34
@author: johannes
"""
from sqlalchemy.orm import Session

from app.sunfeature.model import SunModel
from app.sunfeature.schema import SunBase
from app.core.db.association_tables import SunMoonModel

COLUMNS = {'created_at', 'sun_number'}


def get_sun(db: Session, sun_number: int):
    return db.query(SunModel).filter(SunModel.sun_number == sun_number).first()


def get_sun_from_id(db: Session, sun_id: int):
    return db.query(SunModel).filter(SunModel.id == sun_id).first()


def get_sun_ids(db: Session, moon_id):
    query = db.query(SunMoonModel).filter(SunMoonModel.moon_id == moon_id).all()
    return [sun.id for sun in query]


def upsert_sun(db: Session, sun: SunBase):
    db_sun = get_sun(db=db, sun_number=sun.sun_number)
    if db_sun:
        return db_sun
    else:
        try:
            db_sun = SunModel(**{c: sun.get(c) for c in COLUMNS})
            db.add(db_sun)
            db.commit()
            db.refresh(db_sun)
            return db_sun
        except Exception as e:
            raise e
