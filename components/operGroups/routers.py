from fastapi import APIRouter, Cookie, Response, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.operGroups import crud, schemas
from db.database import get_db
import hashlib
from configparser import ConfigParser


configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/operGroups',
    tags=['operGroups']
)


@router.post('/create', response_model=schemas.IdOperGroup)
def create(base: schemas.CreateChangeOperGroup, db: Session = Depends(get_db)):
    return crud.create(db=db, opergroup=base)


@router.put('/change/{id}')
def change():
    pass


@router.delete('/delete/{id}')
def hide():
    pass


@router.patch('/undelete/{id}')
def show():
    pass


@router.get('/list')
def get_list():
    pass


@router.get('/features/{id}')
def get_features():
    pass


@router.get('/printerList/{id}')
def get_printer_list():
    pass


@router.put('/addPrinter/{id}')
def add_printers():
    pass


@router.put('/deletePrinters')
def delete_printers():
    pass

