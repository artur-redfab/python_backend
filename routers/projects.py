from fastapi import APIRouter, Cookie, Response, Depends, HTTPException
from sqlalchemy.orm import Session
from models import crud, schemas
from models.database import get_db
import hashlib


router = APIRouter(
    prefix='/hs/project',
    tags=['project']
)


@router.post("/create")
def create_project():
    pass


@router.put("/change/{id}")
def change_project():
    pass


@router.delete("/delete/{id}")
def hide_project():
    pass


@router.patch("/undelete/{id}")
def show_project():
    pass


@router.post("/list")
def get_projects_list():
    pass


@router.get("/features/{id}")
def get_features():
    pass


@router.post("/taskList/{id}")
def get_project_list():
    pass


@router.put("/set/{id}")
def set_status():
    pass


@router.post("/createPrototype/{id}")
def create_prototype():
    pass

