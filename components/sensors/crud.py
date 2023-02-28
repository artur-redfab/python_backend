from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.sensors import schemas, models
from components.projects.routers import configP


def get_sensors(db: Session, sort: schemas.SortSensors):
    if not hasattr(models.Sensors, sort.sortBy):
        return JSONResponse(status_code=200, content=configP.get('sensors', 'sort_error'))
    attr = getattr(models.Sensors, sort.sortBy)
    db_sensors = db.query(models.Sensors)
    if sort.direction == "DESC":
        db_sensors = db_sensors.order_by(attr.desc())
    else:
        db_sensors = db_sensors.order_by(attr.asc())
    db_sensors = db_sensors.offset(sort.offset).limit(sort.limit).all()
    return db_sensors


def get_groups(db: Session):
    db_groups = db.query(models.SensorsGroups).all()
    return db_groups


def get_feature_by_id(id: int, db: Session):
    db_feature = db.query(models.Sensors).filter(models.Sensors.id == id).first()
    return db_feature

