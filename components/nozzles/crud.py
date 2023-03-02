from sqlalchemy.orm import Session
from components.nozzles import models


def get_types_list(db: Session):
    db_types = db.query(models.NozzleTypes).all()
    return db_types


def get_type_by_id(id: int, db: Session):
    db_type = db.query(models.NozzleTypes).filter(models.NozzleTypes.id == id).first()
    return db_type


def get_sizes_list(db: Session):
    db_sizes = db.query(models.NozzleSizes).all()
    return db_sizes


def get_size_by_id(id: int, db: Session):
    db_size = db.query(models.NozzleSizes).filter(models.NozzleSizes.id == id).first()
    return db_size

