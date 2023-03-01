from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.partners import crud, schemas
from components.tasks import schemas as tasks_schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/partner',
    tags=['partners']
)


@router.post('/create', response_model=schemas.IdPartner)
def create_partner(base: schemas.CreatePartner, db: Session = Depends(get_db)) -> schemas.IdPartner:
    return crud.create_partner(db=db, partner=base)


@router.put('/change/{id}')
def change_partner():
    pass


@router.delete('/delete/{id}')
def hide_partner():
    pass


@router.patch('/undelete/{id}')
def show_partner():
    pass


@router.post('/list')
def list_partners():
    pass


@router.get('/features/{id}')
def get_features():
    pass

