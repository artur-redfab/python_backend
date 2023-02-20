from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.projects import crud, schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='',
    tags=['']
)




