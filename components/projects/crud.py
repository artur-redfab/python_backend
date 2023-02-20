from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.users import models as users_models
from components.projects import schemas, models
from components.materials.routers import configP


def create_project(db: Session, project: schemas.CreateProject):
    db_project = models.Projects(
        name=project.name,
        idPriority=project.idPriority,
        deadLine=project.deadLine,
        orderNumber=project.orderNumber,
        idPartner=project.idPartner,
        idResponsible=project.idResponsible,
        idAuthor=project.idAuthor,
        comment=project.comment
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    query = get_project_features(db=db, project_id=db_project.id)
    return query


def get_project_by_id(project_id: int, db: Session):
    db_project = db.query(models.Projects).filter(models.Projects.id == project_id).first()
    return db_project


def change_project(db: Session, new_project_data: schemas.ChangeProject, project_id: int):
    db_project = db.query(models.Projects).filter(models.Projects.id == project_id).first()
    db_project.name = new_project_data.name
    db_project.idPriority = new_project_data.idPriority
    db_project.deadLine = new_project_data.deadLine
    db_project.orderNumber = new_project_data.orderNumber
    db_project.idPartner = new_project_data.idPartner
    db_project.idResponsible = new_project_data.idResponsible
    db_project.comment = new_project_data.comment
    db.commit()


def hide_project(db: Session, project_id: int):
    db_project = db.query(models.Projects).filter(models.Projects.id == project_id).first()
    db_project.markingDeletion = True
    db.commit()


def show_project(db: Session, project_id: int):
    db_project = db.query(models.Projects).filter(models.Projects.id == project_id).first()
    db_project.markingDeletion = False
    db.commit()


def get_projects(sort: schemas.SortProjects, db: Session):
    if not hasattr(models.Projects, sort.sortBy):
        return JSONResponse(status_code=200, content=configP.get('projects', 'sort_error'))
    attr = getattr(models.Projects, sort.sortBy)
    db_query = db.query(
        models.Projects.id,
        models.Projects.name,
        models.Projects.idPriority,
        models.Projects.orderNumber,
        models.Projects.idPartner,
        # TODO: models.Partners.name.label('partner')
        models.Projects.idResponsible,
        users_models.Users.name.label('responsible'),
        models.Projects.markingDeletion
    ) \
        .join(users_models.Users, users_models.Users.id == models.Projects.idResponsible)
    # TODO: .join(models.Partners, models.Partners.id == models.Project.idPartner)
    if sort.direction == "DESC":
        db_query = db_query.order_by(attr.desc()).offset(sort.offset).limit(sort.limit).all()
    else:
        db_query = db_query.order_by(attr.asc()).offset(sort.offset).limit(sort.limit).all()
    return db_query


def get_project_features(project_id: int, db: Session):
    query = db.query(
        models.Projects.id,
        models.Projects.name,
        models.Projects.idPriority,
        models.Projects.createDate,
        models.Projects.deadLine,
        models.Projects.changeDate,
        models.Projects.orderNumber,
        models.Projects.idPartner,
        models.Projects.idResponsible,
        users_models.Users.name.label('author'),
        # models.ProjectStatusHistory.idProjectStatus # TODO!!!!
        models.Projects.comment,
        models.Projects.markingDeletion
    ).join(users_models.Users, users_models.Users.id == models.Projects.idAuthor) \
        .filter(models.Projects.id == project_id).first()
    return query

