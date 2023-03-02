from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.makers import crud, schemas
from db.database import get_db
from configparser import ConfigParser


configP = ConfigParser()
configP.read('messages.ini')

router = APIRouter(
    prefix='/hs/nozzlesSizes',
    tags=['nozzlesSizes']
)


@router.get('/list')
def get_list_nozzles_sizes(

):
    pass


@router.get('/features/{id}')
def get_features(

):
    pass

