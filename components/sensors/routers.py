from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.printers import crud, schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/sensor',
    tags=['sensor']
)


@router.post('/list')
def get_sensors():
    pass


@router.get('/groups')
def get_groups():
    pass


@router.get('/features/{id}')
def get_features():
    pass


@router.post('/data/{id}')
def get_sensors_history()
    pass
