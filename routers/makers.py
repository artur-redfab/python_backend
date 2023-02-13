from fastapi import APIRouter, Cookie, Response, Depends, HTTPException
from sqlalchemy.orm import Session
from models import crud, schemas
from models.database import get_db

router = APIRouter(
    prefix='/hs/makers',
    tags=['makers']
)


@router.post("/create", response_model=schemas.MakerId)
def create_maker(maker: schemas.MakerName, db: Session = Depends(get_db)):
    return crud.create_maker(db=db, maker=maker)


@router.put("/change/{id}", response_status=200)
def change_maker(maker: schemas.MakerId, db: Session = Depends(get_db)):



@router.delete("/delete/{id}")
def hide_maker():
    pass


@router.patch("/undelete/{id}")
def show_maker():
    pass


@router.get("/list")
def get_makers_list():
    pass


@router.get("/features/{id}")
def get_features():
    pass

