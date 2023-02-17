import hashlib
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from models import schemas, models


def get_color(db: Session, id: int):
    return db.query(models.Color).filter(models.Color.id == id).first()


def get_colors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Color).offset(skip).limit(limit).all()


def create_color(db: Session, color: schemas.ColorCreate):
    db_color = models.Color(email=color.name, additionalCleaning=color.additionalCleaning)
    db.add(db_color)
    db.commit()
    db.refresh(db_color)
    return db_color


# def set_color(db: Session, id: int):
#     db_color = db.query(models.Color).filter(models.Color.id == id).first()
#     db_color.update({'name': '12345'})
#     db.commit()
#     # db.refresh(db_color)
#     return db_color

def set_color(db: Session, id: int, name: str):
    update_color = db.query(models.Color).filter(models.Color.id == id).first()
    update_color.name = name
    db.commit()


def get_features(id: int, db: Session):
    return db.query(models.Color).filter(models.Color.id == id).first()


# методы для работы с моделью Users
def create_user(db: Session, user: schemas.User):
    passwordHash = str(hashlib.md5(str.encode(user.password, encoding='utf-8')).hexdigest())
    db_user = models.Users(
        name=user.name,
        firstname=user.firstname,
        login=user.login,
        passwordHash=passwordHash,
        idRole=user.idRole,
        position=user.position
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, user_id: int):
    db_user = db.query(models.Users).filter(models.Users.id == user_id).first()
    return db_user


def get_user_by_login(db: Session, login: str):
    db_user = db.query(models.Users).filter(models.Users.login == login).first()
    return db_user


# Уточнить по универсальности метода, он возвращает не все поля БД
def get_users(db: Session, user_id=None):
    if user_id:
        db_users = db.query(
            models.Users.id,
            models.Users.name,
            models.Users.login,
            models.Users.idRole,
            models.Users.markingDeletion
        ).filter(models.Users.id == user_id).all()
    else:
        db_users = db.query(
            models.Users.id,
            models.Users.name,
            models.Users.login,
            models.Users.idRole,
            models.Users.markingDeletion
        ).order_by(models.Users.id).all()
    return db_users


def get_users_role_list(db: Session):
    db_users_role_list = db.query(
        models.Users.id,
        models.Users.idRole
    ).order_by(models.Users.id).all()
    return db_users_role_list


def change_user(db: Session, user_id: int, new_user_data: schemas.User):
    passwordHash = str(hashlib.md5(str.encode(new_user_data.password, encoding='utf-8')).hexdigest())
    db_user = get_user_by_id(db=db, user_id=user_id)
    db_user.name = new_user_data.name
    db_user.idRole = new_user_data.idRole
    db_user.passwordHash = passwordHash
    db_user.position = new_user_data.position
    db_user.firstname = new_user_data.firstname
    db_user.login = new_user_data.login
    db.commit()


def hide_user(db: Session, user_id: int):
    db_user = get_user_by_id(db=db, user_id=user_id)
    db_user.markingDelete = True
    db.commit()


def show_user(db: Session, user_id: int):
    db_user = get_user_by_id(db=db, user_id=user_id)
    db_user.markingDelete = False
    db.commit()


def get_features_by_user_id(db: Session, user_id: int):
    db_user = db.query(
        models.Users.id,
        models.Users.name,
        models.Users.firstname,
        models.Users.login,
        models.Users.idRole,
        models.Users.position,
        models.Users.markingDeletion
    ).filter(models.Users.id == user_id).first()
    return db_user


# методы для работы с моделью Projects
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
        return JSONResponse(status_code=400, content="Sort error")
    attr = getattr(models.Projects, sort.sortBy)
    db_query = db.query(
        models.Projects.id,
        models.Projects.name,
        models.Projects.idPriority,
        models.Projects.orderNumber,
        models.Projects.idPartner,
        # TODO: models.Partners.name.label('partner')
        models.Projects.idResponsible,
        models.Users.name.label('responsible'),
        models.Projects.markingDeletion
    ) \
        .join(models.Users, models.Users.id == models.Projects.idResponsible)
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
        models.Users.name.label('author'),
        # models.ProjectStatusHistory.idProjectStatus # TODO!!!!
        models.Projects.comment,
        models.Projects.markingDeletion
    ).join(models.Users, models.Users.id == models.Projects.idAuthor) \
        .filter(models.Projects.id == project_id).first()
    return query
