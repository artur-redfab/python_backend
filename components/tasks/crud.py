from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.tasks import schemas, models


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
    return new_task.id

