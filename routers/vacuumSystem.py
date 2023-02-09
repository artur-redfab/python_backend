from fastapi import APIRouter, Cookie, Response, Depends, HTTPException
from sqlalchemy.orm import Session
from models import crud, schemas
from models.database import get_db
import hashlib


router = APIRouter(
    prefix='/hs/vacuumSystem',
    tags=['vacuumSystem']
)


@router.post("/create")
def create_vacuum_system():
    pass


@router.put("/change")
def change_vacuum_system():
    pass


@router.delete("/delete/{id}")
def hide_vacuum_system():
    pass


@router.patch("/undelete/{id}")
def show_vacuum_system():
    pass


@router.get("/list")
def get_vacuum_systems():
    pass


@router.get("/features/{id}")
def get_features():
    pass

