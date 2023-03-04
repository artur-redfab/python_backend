from sqlalchemy.orm import Session
from components.tasks import schemas, models
from components.projects import models as projects_models
from components.materials import models as materials_models
from components.colors import models as colors_models
from components.nozzles import models as nozzles_models
from components.operGroups import models as opergroups_models
from components.taskFiles import models as taskfiles_models


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
        nozzles_models.NozzleTypes.id.label('idNozzleType'),
        nozzles_models.NozzleTypes.name.label('nozzleType'),
        nozzles_models.NozzleSizes.id.label('idNozzleSize'),
        nozzles_models.NozzleSizes.nozzlesSize.label('nozzleSize'),
        models.Tasks.idOperGroup,
        opergroups_models.OperGroups.name.label('operGroup'),
        taskfiles_models.TaskFiles.id.label('idFile'),
        taskfiles_models.TaskFiles.nameFile,
        taskfiles_models.TaskFiles.extFile,
        taskfiles_models.TaskFiles.sizeFile,
        taskfiles_models.TaskFiles.hashFile,
        models.Tasks.volume,
        models.Tasks.markingDeletion
    ).join(projects_models.Projects, projects_models.Projects.id == models.Tasks.idProject)\
     .join(materials_models.Materials, materials_models.Materials.id == models.Tasks.idBasicMaterial) \
     .join(colors_models.Color, colors_models.Color.id == models.Tasks.idBasicColor) \
     .join(opergroups_models.OperGroups, opergroups_models.OperGroups.id == models.Tasks.idOperGroup) \
     .join(nozzles_models.NozzleTypes, nozzles_models.NozzleTypes.id == opergroups_models.OperGroups.idNozzleType) \
     .join(nozzles_models.NozzleSizes, nozzles_models.NozzleSizes.id == opergroups_models.OperGroups.idNozzleSize) \
     .join(taskfiles_models.TaskFiles, taskfiles_models.TaskFiles.idTask == models.Tasks.id) \
     .filter(models.Tasks.id == task_id).first()
    return query


def change_task_status(db: Session, task_id: int, task_stat: schemas.IdTaskStatus):
    history = models.TaskStatusHistory(
        idTask=task_id,
        idTaskStatus=task_stat.idTaskStatus
    )
    db.add(history)
    db.commit()
    db.refresh(history)


def get_task_copy_by_id(db: Session, id_copy: int):
    db_copy = db.query(models.TasksCopies).filter(models.TasksCopies.id == id_copy).first()
    return db_copy


def change_copy_status(db: Session, copy, status: int):
    copy.idTaskStatus = status
    db.commit()

