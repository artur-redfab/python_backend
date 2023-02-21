from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.tasks import schemas, models
from components.projects import models as projects_models
from components.materials import models as materials_models
from components.colors import models as colors_models


def create(db: Session, task: schemas.CreatingChangingTask):
    new_task = models.Tasks(
        name=task.name,
        idProject=task.idProject,
        idPriority=task.idPriority,
        numberCopies=task.numberCopies,
        planPrintTime=task.planPrintTime,
        twoExtrPrint=task.twoExtrPrint,
        idBasicMaterial=task.idBasicMaterial,
        idSupportMaterial=task.idSupportMaterial,
        idBasicColor=task.idBasicColor,
        idSupportColor=task.idSupportColor,
        idOperGroup=task.idOperGroup,
        volume=task.volume
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    query = db.query(models.Tasks.id).filter(models.Tasks.id == new_task.id).first()
    return query


def get_task_by_id(db: Session, task_id: int):
    db_task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    return db_task


def change(db: Session, new_task_data: schemas.CreatingChangingTask, task_id: int):
    db_task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    db_task.name = new_task_data.name
    db_task.idProject = new_task_data.idProject
    db_task.idPriority = new_task_data.idPriority
    db_task.numberCopies = new_task_data.numberCopies
    db_task.planPrintTime = new_task_data.planPrintTime
    db_task.twoExtrPrint = new_task_data.twoExtrPrint
    db_task.idBasicMaterial = new_task_data.idBasicMaterial
    db_task.idSupportMaterial = new_task_data.idSupportMaterial
    db_task.idBasicColor = new_task_data.idBasicColor
    db_task.idSupportColor = new_task_data.idSupportColor
    db_task.idOperGroup = new_task_data.idOperGroup
    db_task.volume = new_task_data.volume
    db.commit()


def hide(db: Session, task_id: int):
    db_task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    db_task.markingDeletion = True
    db.commit()


def show(db: Session, task_id: int):
    db_task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    db_task.markingDeletion = False
    db.commit()


def get_features(task_id: int, db: Session):
    query = db.query(
        models.Tasks.id,
        models.Tasks.name,
        models.Tasks.idProject,
        projects_models.Projects.name.label('project'),
        models.Tasks.idPriority,
        models.Tasks.numberCopies,
        models.Tasks.planPrintTime,
        models.Tasks.factPrintTime,
        models.Tasks.twoExtrPrint,
        models.Tasks.idBasicMaterial,
        materials_models.Materials.name.label('basicMaterial'),
        models.Tasks.idBasicColor,
        colors_models.Color.name.label('basicColor'),
        models.Tasks.idSupportMaterial,
        materials_models.Materials.name.label('supportMaterial'),
        models.Tasks.idSupportColor,
        colors_models.Color.name.label('supportColor'),
        # TODO: idNozzleType
        # TODO: nozzleType
        # TODO: idNozzleSize
        # TODO: nozzleSize
        models.Tasks.idOperGroup,
        # TODO: operGroups_models.OperGroups.name.label('operGroup')
        # TODO: idFile
        # TODO: nameFile
        # TODO: extFile
        # TODO: sizeFile
        # TODO: hashFile
        models.Tasks.volume,
        models.Tasks.markingDeletion
    ).join(projects_models.Projects, projects_models.Projects.id == models.Tasks.idProject)\
     .join(materials_models.Materials, materials_models.Materials.id == models.Tasks.idBasicMaterial) \
     .join(colors_models.Color, colors_models.Color.id == models.Tasks.idBasicColor) \
     .filter(models.Tasks.id == task_id).first()
    return query


def change_task_status(db: Session, task_id: int, task_stat: int):
    db_last_task = db.query(models.TaskStatusHistory).filter(models.TaskStatusHistory.idTask == task_id).order_by(models.TaskStatusHistory.id.desc()).first()
    db_last_task.idTaskStatus = task_stat
    db.commit()


def change_cope_status(db: Session, task_id: int):
    pass