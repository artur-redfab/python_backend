from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.users import models as users_models
from components.projects import schemas, models
from components.tasks import models as tasks_models
from components.materials import models as materials_models
from components.colors import models as colors_models
from components.partners import models as partners_models
from components.operGroups import models as opergroups_models
from components.nozzles import models as nozzles_models
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
        partners_models.Partners.name.label('partner'),
        models.Projects.idResponsible,
        users_models.Users.name.label('responsible'),
        models.Projects.markingDeletion
    ) \
        .join(users_models.Users, users_models.Users.id == models.Projects.idResponsible)\
        .join(partners_models.Partners, partners_models.Partners.id == models.Projects.idPartner)
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
        models.ProjectStatusHistory.idProjectStatus,
        models.Projects.comment,
        models.Projects.markingDeletion
    ).join(users_models.Users, users_models.Users.id == models.Projects.idAuthor) \
        .filter(models.Projects.id == project_id).first()
    return query


def get_tasks_by_project_id(prj_id: int, sort: schemas.SortProjects, db: Session):
    if not hasattr(tasks_models.Tasks, sort.sortBy):
        return JSONResponse(status_code=200, content=configP.get('tasks', 'sort_error'))
    attr = getattr(tasks_models.Tasks, sort.sortBy)
    db_tasks = db.query(
        tasks_models.Tasks.id,
        tasks_models.Tasks.name,
        tasks_models.Tasks.numberCopies,
        opergroups_models.OperGroups.name.label('operGroup'),
        materials_models.Materials.name.label('basicMaterial'),
        colors_models.Color.colorMaterialHEX.label('basicColorHEX'),
        nozzles_models.NozzleTypes.name.label('nozzleType'),
        nozzles_models.NozzleSizes.nozzlesSize.label('nozzleSize'),
        tasks_models.Tasks.planPrintTime,
        tasks_models.Tasks.factPrintTime,
        tasks_models.Tasks.volume,
        tasks_models.Tasks.markingDeletion
    ).filter(tasks_models.Tasks.idProject == prj_id)\
     .join(materials_models.Materials, materials_models.Materials.id == tasks_models.Tasks.idBasicMaterial)\
     .join(colors_models.Color, colors_models.Color.id == tasks_models.Tasks.idBasicColor)\
     .join(opergroups_models.OperGroups, opergroups_models.OperGroups.id == tasks_models.Tasks.idOperGroup)\
     .join(nozzles_models.NozzleTypes, nozzles_models.NozzleTypes.id == opergroups_models.OperGroups.idNozzleType)\
     .join(nozzles_models.NozzleSizes, nozzles_models.NozzleSizes.id == opergroups_models.OperGroups.idNozzleSize)
    if sort.direction == "DESC":
        db_tasks = db_tasks.order_by(attr.desc()).offset(sort.offset).limit(sort.limit).all()
    else:
        db_tasks = db_tasks.order_by(attr.asc()).offset(sort.offset).limit(sort.limit).all()
    return db_tasks


def change_project_status(prj_id: int, prj_stat: schemas.IdProjectStatus, db: Session):
    history = models.ProjectStatusHistory(
        idProject=prj_id,
        idProjectStatus=prj_stat.idProjectStatus
    )
    db.add(history)
    db.commit()
    db.refresh(history)


def create_project_prototype(project, db: Session):
    prototype = models.Projects(
        name=str(project.name) + '_prototype',
        idPriority=1,
        deadLine=project.deadLine,
        orderNumber=project.orderNumber,
        idPartner=project.idPartner,
        idResponsible=project.idResponsible,
        idAuthor=project.idAuthor,
        comment=project.comment
    )
    db.add(prototype)
    db.commit()
    db.refresh(prototype)
    db_project_tasks = db.query(tasks_models.Tasks).filter(tasks_models.Tasks.idProject == project.id).all()
    for i in range(len(db_project_tasks)):
        new_task = tasks_models.Tasks(
            name=str(db_project_tasks[i].name) + '_prototype',  # Нужен ли тут постфикс?
            idProject=prototype.id,
            idPriority=prototype.idPriority,
            numberCopies=1,
            planPrintTime=db_project_tasks[i].planPrintTime,
            twoExtrPrint=db_project_tasks[i].twoExtrPrint,
            idBasicMaterial=db_project_tasks[i].idBasicMaterial,
            idSupportMaterial=db_project_tasks[i].idSupportMaterial,
            idBasicColor=db_project_tasks[i].idBasicColor,
            idSupportColor=db_project_tasks[i].idSupportColor,
            idOperGroup=db_project_tasks[i].idOperGroup,
            volume=db_project_tasks[i].volume
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)

