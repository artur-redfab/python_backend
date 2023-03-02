from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.makers import crud, schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')

router = APIRouter(
    prefix='/hs/makers',
    tags=['makers']
)


@router.post("/create")
def create_maker(
        maker: schemas.MakerName, db: Session = Depends(get_db)
) -> schemas.MakerId:
    return crud.create_maker(db=db, maker=maker)
    return JSONResponse(status_code=200, content=configP.get('makers', 'maker_created_success'))


@router.put("/change/{id}", status_code=200)
def change_maker(id: str, maker: schemas.MakerName, db: Session = Depends(get_db)):
    db_maker = crud.get_maker_by_id(db=db, maker_id=id)
    if not db_maker:
        raise HTTPException(status_code=404, detail=configP.get('makers', 'maker_not_found'))
    else:
        crud.change_maker(db=db, new_data_maker=maker, maker_id=id)
        return JSONResponse(status_code=200, content=configP.get('makers', 'maker_changed_success'))


@router.delete("/delete/{id}")
def hide_maker(id: str, db: Session = Depends(get_db)):
    db_maker = crud.get_maker_by_id(db=db, maker_id=id)
    if not db_maker:
        raise HTTPException(status_code=404, detail=configP.get('makers', 'maker_not_found'))
    else:
        crud.hide_maker(db=db, maker_id=id)
        return JSONResponse(status_code=200, content=configP.get('makers', 'maker_deleted'))


@router.patch("/undelete/{id}")
def show_maker(id: str, db: Session = Depends(get_db)):
    db_maker = crud.get_maker_by_id(db=db, maker_id=id)
    if not db_maker:
        raise HTTPException(status_code=404, detail=configP.get('makers', 'maker_not_found'))
    else:
        crud.show_maker(db=db, maker_id=id)
        return JSONResponse(status_code=200, content=configP.get('makers', 'maker_undeleted'))


@router.get("/list")
def get_makers_list(db: Session = Depends(get_db)):
    db_makers = crud.get_makers(db=db)
    return db_makers


@router.get("/features/{id}")
def get_features(id: str, db: Session = Depends(get_db)):
    db_maker = crud.get_maker_by_id(db=db, maker_id=id)
    if not db_maker:
        raise HTTPException(status_code=404, detail=configP.get('makers', 'maker_not_found'))
    else:
        return db_maker
