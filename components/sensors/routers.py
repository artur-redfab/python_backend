from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.sensors import crud, schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/sensor',
    tags=['sensor']
)


@router.post('/list', response_model=list[schemas.Sensor])
def get_sensors(sort: schemas.SortSensors, db: Session = Depends(get_db)):
    return crud.get_sensors(db=db, sort=sort)


@router.get('/groups', response_model=list[schemas.Groups])
def get_groups(db: Session = Depends(get_db)):
    return crud.get_groups(db=db)


@router.get('/features/{id}', response_model=schemas.Features)
def get_features(id: int, db: Session = Depends(get_db)):
    db_sensor = crud.get_feature_by_id(id=id, db=db)
    if not db_sensor:
        raise HTTPException(status_code=404, detail=configP.get('sensors', 'sensor_not_found'))
    else:
        return db_sensor

