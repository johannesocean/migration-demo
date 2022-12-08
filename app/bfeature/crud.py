"""
Created on 2022-12-08 15:34
@author: johannes
"""
from random import sample
from typing import List
from sqlalchemy.orm import Session

from app.bfeature.model import BModel
from app.afeature.schema import ABase
from app.bfeature.schema import BBase
from app.core.db.association_tables import ABModel
from app.afeature.crud import upsert_a

COLUMNS = {'created_at', 'number'}


def get_b(db: Session, b_number: int):
    return db.query(BModel).filter(BModel.number == b_number).first()


def get_b_from_id(db: Session, b_id: int):
    return db.query(BModel).filter(BModel.id == b_id).first()


def get_b_id(db: Session, b_id):
    query = db.query(ABModel).filter(ABModel.b_id == b_id).all()
    return [b.b_id for b in query]


def create_b(db: Session, b: BBase, alist: List[ABase]):
    db_b = BModel(**{c: b.get(c) for c in COLUMNS})
    for a in alist:
        updated_a = upsert_a(db, a)
        if updated_a not in db_b.a:
            db_b.a.append(updated_a)
    db.add(db_b)
    db.commit()
    db.refresh(db_b)
    return db_b


def create_b_extracted(db: Session, b: BBase):
    a_list = [
        ABase(**ent) for ent in [
            {'number': sample(range(1, 1000), 10)}
        ]
    ]
    return create_b(db=db, b=b, alist=a_list)


def create_bs(db: Session, bs):
    return [
        create_b_extracted(db=db, b=BBase(**b.dict))
        for b in bs
    ]
