from fastapi import APIRouter, Cookie, Response, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.users import crud, schemas
from db.database import get_db
import hashlib
from configparser import ConfigParser


configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/operGroups',
    tags=['operGroups']
)


@router.post('/create')
def create():
    pass


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


@router.put('/addPrinters/{id}')
def add_printers():
    pass


@router.put('/deletePrinters')
def delete_printers():
    pass

