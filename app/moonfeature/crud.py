"""
Created on 2022-12-08 15:34
@author: johannes
"""
from random import sample
from typing import List
from sqlalchemy.orm import Session

from app.moonfeature.model import MoonModel
from app.sunfeature.schema import SunBase
from app.moonfeature.schema import MoonBase
from app.core.db.association_tables import SunMoonModel
from app.sunfeature.crud import upsert_sun

COLUMNS = {'created_at', 'number'}


def get_moon(db: Session, moon_number: int):
    return db.query(MoonModel).filter(MoonModel.number == moon_number).first()


def get_moon_from_id(db: Session, moon_id: int):
    return db.query(MoonModel).filter(MoonModel.id == moon_id).first()


def get_moon_id(db: Session, moon_id):
    query = db.query(SunMoonModel).filter(SunMoonModel.moon_id == moon_id).all()
    return [moon.moon_id for moon in query]


def create_moon(db: Session, moon: MoonBase, sunlist: List[SunBase]):
    db_moon = MoonModel(**{c: moon.get(c) for c in COLUMNS})
    for sun in sunlist:
        updated_sun = upsert_sun(db, sun)
        if updated_sun not in db_moon.sun:
            db_moon.sun.append(updated_sun)
    db.add(db_moon)
    db.commit()
    db.refresh(db_moon)
    return db_moon


def create_moon_extracted(db: Session, moon: MoonBase):
    sunlist = [
        SunBase(**ent) for ent in [
            {'sun_number': sample(range(1, 1000), 10)}
        ]
    ]
    return create_moon(db=db, moon=moon, sunlist=sunlist)


def create_moons(db: Session, moons):
    return [
        create_moon_extracted(db=db, moon=MoonBase(**moon.dict))
        for moon in moons
    ]
