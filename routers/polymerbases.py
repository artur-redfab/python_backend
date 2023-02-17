from fastapi import APIRouter, Cookie, Response, Depends, HTTPException
from sqlalchemy.orm import Session
from db import crud_old, schemas, models
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')

router = APIRouter(
    prefix="/hs/polymerBase",
    tags=["polymerBase"]
)


@router.get("/list", status_code=200)
def get_polymer_list(db: Session = Depends(get_db)):
    db_polymers = db.query(models.PolymerBases).all()
    return db_polymers


@router.get("/features/{id}", status_code=200)
def get_features(id: int, db: Session = Depends(get_db)):
    db_polymer = db.query(models.PolymerBases).filter(models.PolymerBases.id == id).first()
    if not db_polymer:
        raise HTTPException(status_code=404, detail=configP.get('polymerBases', 'pb_not_found'))
    else:
        return db_polymer
