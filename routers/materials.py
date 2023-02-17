from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db import crud_old, schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/material',
    tags=['material']
)


@router.post("/create", response_model=schemas.MaterialId)
def create_material(material: schemas.Material, db: Session = Depends(get_db)):
    return crud.create_material(db=db, material=material)


@router.put("/change/{id}")
def change_material(id: int, material: schemas.Material, db: Session = Depends(get_db)):
    db_material = crud.get_material_by_id(db=db, mat_id=id)
    if not db_material:
        raise HTTPException(status_code=404, detail=configP.get('materials', 'material_not_found'))
    else:
        crud.change_material(db=db, mat_id=id, new_data_material=material)
        return JSONResponse(status_code=200, content=configP.get('materials', 'material_changed_success'))


@router.delete("/delete/{id}")
def hide_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.get_material_by_id(db=db, mat_id=id)
    if not db_material:
        raise HTTPException(status_code=404, detail=configP.get('materials', 'material_not_found'))
    else:
        crud.hide_material(db=db, mat_id=id)
        return JSONResponse(status_code=200, content=configP.get('materials', 'material_deleted'))


@router.patch("/undelete/{id}")
def show_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.get_material_by_id(db=db, mat_id=id)
    if not db_material:
        raise HTTPException(status_code=404, detail=configP.get('materials', 'material_not_found'))
    else:
        crud.show_material(db=db, mat_id=id)
        return JSONResponse(status_code=200, content=configP.get('materials', 'material_undeleted'))


@router.post("/list")
def get_materials_list(sort: schemas.SortMaterials, db: Session = Depends(get_db)):
    materials = crud.get_materials(sort=sort, db=db)
    return materials


@router.get("/features/{id}", response_model=schemas.MaterialFeatures)
def get_features(id: int, db: Session = Depends(get_db)):
    db_material = crud.get_material_by_id(db=db, mat_id=id)
    if not db_material:
        raise HTTPException(status_code=404, detail=configP.get('materials', 'material_not_found'))
    else:
        return db_material

