from sqlalchemy.orm import Session
from components.packing import models


def get_packing_by_id(packing_id: int, db: Session):
    package = db.query(models.Packing).filter(models.Packing.id == packing_id).first()
    return package


def get_list_packing(db: Session):
    db_packings = db.query(models.Packing).all()
    return db_packings


def get_features(packing_id: int, db: Session):
    db_packing = db.query(models.Packing).filter(models.Packing.id == packing_id).first()
    return db_packing

