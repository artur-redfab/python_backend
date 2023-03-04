from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.packing import crud, schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/packing',
    tags=['packing']
)


@router.get('/list')
def get_list(
        db: Session = Depends(get_db)
) -> list[schemas.PackingBase]:
    return crud.get_list_packing(db=db)


@router.get('/features/{id}', status_code=200)
def get_features(
        id: int, db: Session = Depends(get_db)
) -> schemas.PackingBase:
    packing = crud.get_packing_by_id(packing_id=id, db=db)
    if not packing:
        raise HTTPException(status_code=404, detail=configP.get('packing', 'packing_not_found'))
    else:
        return packing

