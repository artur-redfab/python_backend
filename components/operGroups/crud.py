from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.operGroups import models, schemas
from components.materials.routers import configP


def create(db: Session, opergroup: schemas.CreateChangeOperGroup):
    new_opergroup = models.OperGroups(
        name=opergroup.name,
        idCluster=opergroup.idCluster,
        idNozzleType=opergroup.idNozzleType,
        idNozzleSize=opergroup.idNozzleSize
    )
    db.add(new_opergroup)
    db.commit()
    db.refresh(new_opergroup)
    opergroup = db.query(models.OperGroups).filter(models.OperGroups.id == new_opergroup.id).first()
    return opergroup


