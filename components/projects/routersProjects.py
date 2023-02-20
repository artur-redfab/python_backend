from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.projects import crud, schemas
from db.database import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


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
        raise HTTPException(status_code=404, detail=configP.get('projects', 'project_not_found'))
    else:
        crud.change_project(db=db, new_project_data=project, project_id=id)
        return JSONResponse(status_code=200, content=configP.get('projects', 'project_changed_success'))


@router.delete("/delete/{id}", status_code=200)
def hide_project(id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(project_id=id, db=db)
    if not db_project:
        raise HTTPException(status_code=404, detail=configP.get('projects', 'project_not_found'))
    else:
        crud.hide_project(db=db, project_id=id)
        return JSONResponse(status_code=200, content=configP.get('projects', 'project_deleted'))


@router.patch("/undelete/{id}", status_code=200)
def show_project(id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(project_id=id, db=db)
    if not db_project:
        raise HTTPException(status_code=404, detail=configP.get('projects', 'project_not_found'))
    else:
        crud.show_project(db=db, project_id=id)
        return JSONResponse(status_code=200, content=configP.get('projects', 'project_undeleted'))


@router.post("/list", response_model=list[schemas.ListProjects])
def get_projects_list(sort: schemas.SortProjects, db: Session = Depends(get_db)):
    return crud.get_projects(db=db, sort=sort)


@router.get("/features/{id}", response_model=schemas.CreatedProject)
def get_features(id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(project_id=id, db=db)
    if not db_project:
        raise HTTPException(status_code=404, detail=configP.get('projects', 'project_not_found'))
    else:
        return crud.get_project_features(project_id=id, db=db)


@router.post("/taskList/{id}")
def get_project_list():
    # TODO: нет модели таблицы tasks
    pass


@router.put("/set/{id}")
def set_status():
    # TODO: нет модели таблицы projectStatus
    pass


@router.post("/createPrototype/{id}")
def create_prototype():
    # TODO: нет модели таблицы prototypes
    pass

