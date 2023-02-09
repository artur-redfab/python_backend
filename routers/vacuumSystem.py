from fastapi import APIRouter, Cookie, Response, Depends, HTTPException
from sqlalchemy.orm import Session
from models import crud, schemas
from models.database import get_db


router = APIRouter(
    prefix='/hs/vacuumSystem',
    tags=['vacuumSystem']
)


@router.post("/create")
def create_vacuum_system(vs: schemas.VacuumSystemChangeCreate, db: Session = Depends(get_db)):
    crud.create_vacuum_system(db=db, vs=vs)
    return {"message": "creating_success"}


@router.put("/change/{id}", status_code=200)
def change_vacuum_system(id: int, vs: schemas.VacuumSystemChangeCreate, db: Session = Depends(get_db)):
    db_vs = crud.get_vacuum_system_by_id(db=db, vs_id=id)
    if not db_vs:
        raise HTTPException(status_code=404, detail="По GUID не найден")
    else:
        crud.change_vacuum_system(db=db, new_data_vs=vs, vs_id=id)
        return {"message": "changing_success"}


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

