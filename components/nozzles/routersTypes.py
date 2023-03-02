from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.nozzles import crud, schemas
from db.database import get_db
from configparser import ConfigParser


configP = ConfigParser()
configP.read('messages.ini')

router = APIRouter(
    prefix='/hs/nozzlesType',
    tags=['nozzlesType']
)


@router.get('/list', response_model=list[schemas.NozzleTypesBase])
def get_nozzles_types_list(db: Session = Depends(get_db)):
    return crud.get_types_list(db=db)


@router.get('/features/{id}', response_model=schemas.NozzleTypesFeatures)
def get_features(id: int, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_id(id=id, db=db)
    if not db_type:
        raise HTTPException(status_code=404, detail=configP.get('nozzles', 'nozzle_type_not_found'))
    else:
        return db_type

