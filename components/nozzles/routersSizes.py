from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.nozzles import crud, schemas
from db.database import get_db
from configparser import ConfigParser


configP = ConfigParser()
configP.read('messages.ini')

router = APIRouter(
    prefix='/hs/nozzlesSizes',
    tags=['nozzlesSizes']
)


@router.get('/list', response_model=list[schemas.NozzleSizesBase])
def get_nozzles_types_list(db: Session = Depends(get_db)):
    return crud.get_sizes_list(db=db)


@router.get('/features/{id}', response_model=schemas.NozzleSizesBase)
def get_features(id: int, db: Session = Depends(get_db)):
    db_size = crud.get_size_by_id(id=id, db=db)
    if not db_size:
        raise HTTPException(status_code=404, detail=configP.get('nozzles', 'nozzle_size_not_found'))
    else:
        return db_size

