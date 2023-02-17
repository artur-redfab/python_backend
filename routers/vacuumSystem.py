from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db import crud_old, schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')

router = APIRouter(
    prefix='/hs/vacuumSystem',
    tags=['vacuumSystem']
)


@router.post("/create")
def create_vacuum_system(vs: schemas.VacuumSystemChangeCreate, db: Session = Depends(get_db)):
    crud.create_vacuum_system(db=db, vs=vs)
    return JSONResponse(status_code=200, content=configP.get('vacuum_systems', 'vs_created_success'))


@router.put("/change/{id}", status_code=200)
def change_vacuum_system(id: int, vs: schemas.VacuumSystemChangeCreate, db: Session = Depends(get_db)):
    db_vs = crud.get_vacuum_system_by_id(db=db, vs_id=id)
    if not db_vs:
        raise HTTPException(status_code=404, detail=configP.get('vacuum_systems', 'vs_not_found'))
    else:
        crud.change_vacuum_system(db=db, new_data_vs=vs, vs_id=id)
        return JSONResponse(status_code=200, content=configP.get('vacuum_systems', 'vs_changed_success'))


@router.delete("/delete/{id}", status_code=200)
def hide_vacuum_system(id: int, db: Session = Depends(get_db)):
    db_vs = crud.get_vacuum_system_by_id(db=db, vs_id=id)
    if not db_vs:
        raise HTTPException(status_code=404, detail=configP.get('vacuum_systems', 'vs_not_found'))
    else:
        crud.hide_vacuum_system(db=db, vs_id=id)
        return JSONResponse(status_code=200, content=configP.get('vacuum_systems', 'vs_deleted'))


@router.patch("/undelete/{id}")
def show_vacuum_system(id: int, db: Session = Depends(get_db)):
    db_vs = crud.get_vacuum_system_by_id(db=db, vs_id=id)
    if not db_vs:
        raise HTTPException(status_code=404, detail=configP.get('vacuum_systems', 'vs_not_found'))
    else:
        crud.show_vacuum_system(db=db, vs_id=id)
        return JSONResponse(status_code=200, content=configP.get('vacuum_systems', 'vs_undeleted'))


@router.get("/list")
def get_vacuum_systems_list(db: Session = Depends(get_db)):
    db_vs = crud.get_list_vacuum_systems(db=db)
    return db_vs


@router.get("/features/{id}")
def get_features(id: int, db: Session = Depends(get_db)):
    db_vs = crud.get_vacuum_system_by_id(db=db, vs_id=id)
    if not db_vs:
        raise HTTPException(status_code=404, detail=configP.get('vacuum_systems', 'vs_not_found'))
    else:
        return db_vs

