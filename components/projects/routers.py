from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from components.projects import crud, schemas
from components.tasks import schemas as tasks_schemas
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


@router.post("/taskList/{id}", response_model=list[tasks_schemas.TasksList])
def get_project_list(id: int, sort: schemas.SortProjects, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(db=db, project_id=id)
    if not db_project:
        raise HTTPException(status_code=404, detail=configP.get('projects', 'project_not_found'))
    else:
        return crud.get_tasks_by_project_id(prj_id=id, sort=sort, db=db)


@router.put("/set/{id}", status_code=200)
def set_status(id: int, status: schemas.IdProjectStatus, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(db=db, project_id=id)
    if not db_project:
        raise HTTPException(status_code=404, detail=configP.get('projects', 'project_not_found'))
    else:
        crud.change_project_status(db=db, prj_id=id, prj_stat=status)
        return JSONResponse(status_code=200, content=configP.get('projects', 'project_status_change'))


@router.post("/createPrototype/{id}", status_code=200)
def create_prototype(id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(db=db, project_id=id)
    if not db_project:
        raise HTTPException(status_code=404, detail=configP.get('projects', 'project_not_found'))
    else:
        crud.create_project_prototype(db=db, project=db_project)
        return JSONResponse(status_code=200, content=configP.get('projects', 'project_prototype_created'))

