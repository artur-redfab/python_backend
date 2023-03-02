from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.nozzles import schemas, models


def get_types_list(db: Session):
    db_types = db.query(models.NozzleTypes).all()
    return db_types


def get_type_by_id(id: int, db: Session):
    db_type = db.query(models.NozzleTypes).filter(models.NozzleTypes.id == id).first()
    return db_type

