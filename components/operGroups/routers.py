from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.operGroups import crud, schemas
from components.printers import models as printers_models
from db.database import get_db
from configparser import ConfigParser


configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/operGroups',
    tags=['operGroups']
)


@router.post('/create', response_model=schemas.IdOperGroup)
def create(base: schemas.CreateChangeOperGroup, db: Session = Depends(get_db)):
    return crud.create(db=db, opergroup=base)


@router.put('/change/{id}', status_code=200)
def change(id: int, base: schemas.CreateChangeOperGroup, db: Session = Depends(get_db)):
    opergroup = crud.get_opergroup_by_id(id=id, db=db)
    if not opergroup:
        raise HTTPException(status_code=404, detail=configP.get('oper_group', 'oper_group_not_found'))
    else:
        crud.change(db=db, oper_group=opergroup, new_opergroup=base)
        return JSONResponse(status_code=200, content=configP.get('oper_group', 'oper_group_changed_success'))


@router.delete('/delete/{id}', status_code=200)
def hide(id: int, db: Session = Depends(get_db)):
    opergroup = crud.get_opergroup_by_id(id=id, db=db)
    if not opergroup:
        raise HTTPException(status_code=404, detail=configP.get('oper_group', 'oper_group_not_found'))
    else:
        crud.hide_oper_group(oper_group=opergroup, db=db)
        return JSONResponse(status_code=200, content=configP.get('oper_group', 'oper_group_deleted'))


@router.patch('/undelete/{id}', status_code=200)
def show(id: int, db: Session = Depends(get_db)):
    opergroup = crud.get_opergroup_by_id(id=id, db=db)
    if not opergroup:
        raise HTTPException(status_code=404, detail=configP.get('oper_group', 'oper_group_not_found'))
    else:
        crud.show_oper_group(oper_group=opergroup, db=db)
        return JSONResponse(status_code=200, content=configP.get('oper_group', 'oper_group_undeleted'))


@router.get('/list', response_model=list[schemas.OperGroupList])
def get_list(db: Session = Depends(get_db)):
    return crud.get_oper_groups_list(db=db)


@router.get('/features/{id}', response_model=schemas.OperGroupsBase)
def get_features(id: int, db: Session = Depends(get_db)):
    opergroup = crud.get_opergroup_by_id(id=id, db=db)
    if not opergroup:
        raise HTTPException(status_code=404, detail=configP.get('oper_group', 'oper_group_not_found'))
    else:
        return opergroup


@router.get('/printerList/{id}')
def get_printer_list(id: int, db: Session = Depends(get_db)):
    opergroup = crud.get_opergroup_by_id(id=id, db=db)
    if not opergroup:
        raise HTTPException(status_code=404, detail=configP.get('oper_group', 'oper_group_not_found'))
    else:
        return crud.get_printers_list(oper_group=opergroup, db=db)


@router.put('/addPrinter/{id}')
def add_printers(id: int, printer: schemas.AddPrinter, db: Session = Depends(get_db)):
    opergroup = crud.get_opergroup_by_id(id=id, db=db)
    if not opergroup:
        raise HTTPException(status_code=404, detail=configP.get('oper_group', 'oper_group_not_found'))
    else:
        crud.add_printer(opergroup_id=id, printer_id=printer.id, db=db)
        return JSONResponse(status_code=200, content=configP.get('oper_group', 'oper_group_printer_add_success'))

