from configparser import ConfigParser
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.colors import crud
from components.colors import schemas
from db.database import get_db

# instantiate
configP = ConfigParser()
# parse existing file
configP.read('messages.ini')

cluster_router = APIRouter(
    prefix='/hs/cluster',
    tags=['cluster']
)


@cluster_router.post('/create')
def create():
    pass


@cluster_router.put('/change/{id}')
def change():
    pass


@cluster_router.delete('/delete/{id}')
def hide():
    pass


@cluster_router.patch('/undelete/{id}')
def show():
    pass


@cluster_router.get('/list')
def get_clusters_list():
    pass


@cluster_router.get('/features/{id}')
def get_features():
    pass


@cluster_router.get('/all')
def get_all():
    pass

