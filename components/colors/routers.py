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

router = APIRouter(
    prefix='/hs/color',
    tags=['color']
)


@router.post("/create", response_model=schemas.Color)
def create_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    db_color = crud.get_colors(db)
    if db_color:
        raise HTTPException(status_code=400, detail=configP.get('colors', 'color_already_registered'))
    return crud.create_color(db=db)


@router.patch("/change/{id}", response_model=schemas.ColorUpdate)
def change_color(id: int, color: schemas.ColorUpdate, db: Session = Depends(get_db)):
    db_color = crud.get_color(db, id=id)
    if not db_color:
        raise HTTPException(status_code=400, detail=config.get('colors', 'color_already_registered'))
    crud.set_color(db=db, id=id, name=color.name)
    return crud.get_color(db=db, id=id)


@router.delete("/delete/{id}", response_model=schemas.Color)
def delete_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    db_color = crud.get_colors(db)
    if db_color:
        raise HTTPException(status_code=400, detail="Color already registered")
    return crud.create_color(db=db)


@router.patch("/undelete/{id}", response_model=schemas.Color)
def undelete_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    db_color = crud.set_color(db)
    if db_color:
        raise HTTPException(status_code=400, detail="Color already registered")
    return crud.create_color(db=db)


@router.get("/list", response_model=list[schemas.Color])
def get_colors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    colors = crud.get_colors(db, skip=skip, limit=limit)
    return colors


@router.post("/features/{id}", response_model=schemas.Color)
def create_color(id: int, db: Session = Depends(get_db)):
    db_color = crud.get_features(id=id, db=db)
    if db_color:
        raise HTTPException(status_code=400, detail="Color already registered")
    return crud.create_color(db=db)