from fastapi import APIRouter, Cookie, Response, Depends, HTTPException
from sqlalchemy.orm import Session
from models import crud, schemas
from models.database import get_db
import hashlib


router = APIRouter(
    prefix='/hs/project',
    tags=['project']
)


@router.post("/create", response_model=schemas.CreatedProject)
def create_project(project: schemas.CreateProject, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)


@router.put("/change/{id}", status_code=200)
def change_project(project: schemas.ChangeProject, id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(project_id=id, db=db)
    if not db_project:
        raise HTTPException(status_code=404, detail='По GUID не найден')
    else:
        crud.change_project(db=db, new_project_data=project, project_id=id)
        return {"message": "Изменен"}


@router.delete("/delete/{id}", status_code=200)
def hide_project(id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(project_id=id, db=db)
    if not db_project:
        raise HTTPException(status_code=404, detail='По GUID не найден')
    else:
        crud.hide_project(db=db, project_id=id)
        return {"message": "Изменен"}


@router.patch("/undelete/{id}", status_code=200)
def show_project(id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(project_id=id, db=db)
    if not db_project:
        raise HTTPException(status_code=404, detail='По GUID не найден')
    else:
        crud.show_project(db=db, project_id=id)
        return {"message": "Изменен"}


@router.post("/list", response_model=list[schemas.ListProjects])
def get_projects_list(sort: schemas.SortProjects, db: Session = Depends(get_db)):
    return crud.get_projects(db=db, sort=sort)


@router.get("/features/{id}")
def get_features():
    pass


@router.post("/taskList/{id}")
def get_project_list():
    pass


@router.put("/set/{id}")
def set_status():
    pass


@router.post("/createPrototype/{id}")
def create_prototype():
    pass

