"""
Created on 2022-12-08 15:34
@author: johannes
"""
from sqlalchemy.orm import Session

from app.afeature.model import AModel
from app.afeature.schema import ABase
from app.core.db.association_tables import ABModel

COLUMNS = {'created_at', 'number'}


def get_a(db: Session, a_number: int):
    return db.query(AModel).filter(AModel.number == a_number).first()


def get_a_from_id(db: Session, a_id: int):
    return db.query(AModel).filter(AModel.id == a_id).first()


def get_a_ids(db: Session, b_id):
    query = db.query(ABModel).filter(ABModel.b_id == b_id).all()
    return [a.a_id for a in query]


def upsert_a(db: Session, a: ABase):
    db_a = get_a(db=db, a_number=a.number)
    if db_a:
        return db_a
    else:
        try:
            db_a = AModel(**{c: a.get(c) for c in COLUMNS})
            db.add(db_a)
            db.commit()
            db.refresh(db_a)
            return db_a
        except Exception as e:
            raise e
