"""
Created on 2022-12-08 15:34
@author: johannes
"""
from random import sample
from typing import List
from sqlalchemy.orm import Session

from app.sun.model import SunModel
from app.sun.schema import SunBase
from app.moon.schema import MoonBase
from app.moon.crud import upsert_moon


def get_sun(db: Session, sun_number: int):
    return db.query(SunModel).filter(SunModel.sun_number == sun_number).first()


def create_sun(db: Session, sun: SunBase, moons: List[MoonBase]):
    db_sun = SunModel(**sun.dict())
    for moon in moons:
        updated_moon = upsert_moon(db, moon)
        if updated_moon not in db_sun.moon:
            db_sun.moon.append(updated_moon)
    db.add(db_sun)
    db.commit()
    db.refresh(db_sun)
    return db_sun


def create_sun_extracted(db: Session, sun: SunBase):
    moons = [
        MoonBase(**ent) for ent in [
            {'moon_number': sample(range(1, 1000), 10)}
        ]
    ]
    return create_sun(db=db, sun=sun, moons=moons)


def create_suns(db: Session, suns):
    return [
        create_sun_extracted(db=db, sun=SunBase(**sun.dict))
        for sun in suns
    ]
