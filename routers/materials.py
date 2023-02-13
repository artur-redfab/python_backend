from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import crud, schemas
from models.database import get_db

router = APIRouter(
    prefix='/hs/material',
    tags=['material']
)


@router.post("/create", response_model=schemas.MaterialId)
def create_material(material: schemas.Material, db: Session = Depends(get_db)):
    return crud.create_material(db=db, material=material)


@router.put("/change/{id}")
def change_material():
    pass


@router.delete("/delete/{id}")
def hide_material():
    pass


@router.patch("/undelete/{id}")
def show_material():
    pass


@router.post("/list")
def get_materials_list():
    pass


@router.get("/features/{id}")
def get_features():
    pass