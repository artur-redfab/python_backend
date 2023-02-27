from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from decouple import config

from components.taskFiles import crud as taskFiles_crud
from components.tasks import crud, schemas
from db.database import get_db
from configparser import ConfigParser
from components.FTP import ftp

configP = ConfigParser()
configP.read('messages.ini')


router = APIRouter(
    prefix='/hs/task',
    tags=['task']
)


@router.post("/create", status_code=200)
def create(task: schemas.CreatingChangingTask, db: Session = Depends(get_db)):
    return crud.create(db=db, task=task)


@router.put("/change/{id}")
def change(id: int, task: schemas.CreatingChangingTask, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(db=db, task_id=id)
    if not db_task:
        raise HTTPException(status_code=404, detail=configP.get('tasks', 'task_not_found'))
    else:
        crud.change(db=db, new_task_data=task, task_id=id)
        return JSONResponse(status_code=200, content=configP.get('tasks', 'task_changed_success'))


@router.delete("/delete/{id}")
def hide(id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(task_id=id, db=db)
    if not db_task:
        raise HTTPException(status_code=404, detail=configP.get('tasks', 'task_not_found'))
    else:
        crud.hide(db=db, task_id=id)
        return JSONResponse(status_code=200, content=configP.get('tasks', 'task_deleted'))


@router.patch("/undelete/{id}")
def show(id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(task_id=id, db=db)
    if not db_task:
        raise HTTPException(status_code=404, detail=configP.get('tasks', 'task_not_found'))
    else:
        crud.show(db=db, task_id=id)
        return JSONResponse(status_code=200, content=configP.get('tasks', 'task_undeleted'))


@router.get("/features/{id}", response_model=schemas.Task)
def get_features(id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(task_id=id, db=db)
    if not db_task:
        raise HTTPException(status_code=404, detail=configP.get('tasks', 'task_not_found'))
    else:
        return crud.get_features(db=db, task_id=id)


@router.put("/setStatus/{id}", status_code=200)
def set_task_status(id: int, status: schemas.IdTaskStatus, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(db=db, task_id=id)
    if not db_task:
        raise HTTPException(status_code=404, detail=configP.get('tasks', 'task_not_found'))
    else:
        crud.change_task_status(db=db, task_id=id, task_stat=status)
        return JSONResponse(status_code=200, content=configP.get('tasks', 'task_status_change'))


@router.put("/setStatusItem/{id_task_copy}")
def set_copy_status(id_task_copy: int, status: int, db: Session = Depends(get_db)):
    db_copy = crud.get_task_copy_by_id(db=db, id_copy=id_task_copy)
    if not db_copy:
        raise HTTPException(status_code=404, detail=configP.get('tasks', 'task_copy_not_found'))
    else:
        crud.change_copy_status(db=db, copy=db_copy, status=status)
        return JSONResponse(status_code=200, content=configP.get('tasks', 'task_copy_change'))


@router.post("/createFile/{id}")
def create_file(id: int, file: UploadFile, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(db=db, task_id=id)
    if not db_task:
        raise HTTPException(status_code=404, detail=configP.get('tasks', 'task_copy_not_found'))
    else:
        ftp.send_file_to_FTP(filename=file.filename, dep_path=config('FTP_UPLOAD_PATH'))
        return taskFiles_crud.write_file_data(db=db, task_id=id, file_data=file)

