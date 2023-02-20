from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.tasks import crud, schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/task',
    tags=['task']
)


@router.post("/create", response_model=schemas.IdTask)
def create(task: schemas.CreatingChangingTask, db: Session = Depends(get_db)):
    return crud.create(db=db, task=task)


@router.put("/change/{id}")
def change():
    pass


@router.delete("/delete/{id}")
def hide():
    pass


@router.patch("/undelete/{id}")
def show():
    pass


@router.get("/features/{id}")
def get_features():
    pass


@router.put("/setStatus/{id}")
def set_status():
    pass


@router.put("/setStatusItem/{id}/{itemNumber}")
def set_copy_status():
    pass


@router.post("/createFile/{id}")
def create_file():
    pass


