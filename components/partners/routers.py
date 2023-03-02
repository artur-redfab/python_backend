from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.partners import crud, schemas
from components.tasks import schemas as tasks_schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/partner',
    tags=['partners']
)


@router.post('/create', response_model=schemas.IdPartner)
def create_partner(base: schemas.CreateChangePartner, db: Session = Depends(get_db)):
    return crud.create_partner(db=db, partner=base)


@router.put('/change/{id}', status_code=200)
def change_partner(id: int, base: schemas.CreateChangePartner, db: Session = Depends(get_db)):
    db_partner = crud.get_partner_by_id(db=db, id=id)
    if not db_partner:
        raise HTTPException(status_code=404, detail=configP.get('partners', 'partner_not_found'))
    else:
        crud.change_partner(db=db, partner_id=id, partner=base)
        return JSONResponse(status_code=200, content=configP.get('partners', 'partner_changed_success'))


@router.delete('/delete/{id}', status_code=200)
def hide_partner(id: int, db: Session = Depends(get_db)):
    db_partner = crud.get_partner_by_id(db=db, id=id)
    if not db_partner:
        raise HTTPException(status_code=404, detail=configP.get('partners', 'partner_not_found'))
    else:
        crud.hide_partner(db=db, partner=db_partner)
        return JSONResponse(status_code=200, content=configP.get('partners', 'partner_deleted'))


@router.patch('/undelete/{id}')
def show_partner(id: int, db: Session = Depends(get_db)):
    db_partner = crud.get_partner_by_id(db=db, id=id)
    if not db_partner:
        raise HTTPException(status_code=404, detail=configP.get('partners', 'partner_not_found'))
    else:
        crud.show_partner(db=db, partner=db_partner)
        return JSONResponse(status_code=200, content=configP.get('partners', 'partner_undeleted'))


@router.post('/list', response_model=list[schemas.ListPartners])
def get_partners_list(sort: schemas.SortPartners, db: Session = Depends(get_db)):
    return crud.get_projects(db=db, sort=sort)


@router.get('/features/{id}')
def get_features(
        id: int, db: Session = Depends(get_db)
) -> schemas.ListPartners:
    db_partner = crud.get_partner_by_id(db=db, id=id)
    if not db_partner:
        raise HTTPException(status_code=404, detail=configP.get('partners', 'partner_not_found'))
    else:
        return db_partner


