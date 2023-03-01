from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.projects import crud, schemas
from components.tasks import schemas as tasks_schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/partner',
    tags=['partners']
)


@router.post('/create')
def create_partner(db: Session = Depends(get_db)):
    pass


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

