from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.operGroups import models, schemas
from components.clusters import models as clusters_models
from components.nozzles import models as nozzles_models
from components.printers import models as printers_models
from components.materials.routers import configP
from db.database import get_db


def get_opergroup_by_id(id: int, db: Session):
    opergroup = db.query(models.OperGroups).filter(models.OperGroups.id == id).first()
    return opergroup


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
    return get_opergroup_by_id(id=new_opergroup.id, db=db)


def change(db: Session, oper_group, new_opergroup: schemas.CreateChangeOperGroup):
    oper_group.name = new_opergroup.name
    oper_group.idCluster = new_opergroup.idCluster
    oper_group.idNozzleType = new_opergroup.idNozzleType
    oper_group.idNozzleSize = new_opergroup.idNozzleSize
    db.commit()


def hide_oper_group(oper_group, db: Session):
    oper_group.markingDeletion = True
    db.commit()


def show_oper_group(oper_group, db: Session):
    oper_group.markingDeletion = False
    db.commit()


def get_oper_groups_list(db: Session):
    query = db.query(
        models.OperGroups.id,
        models.OperGroups.name,
        clusters_models.Clusters.name.label('cluster'),
        nozzles_models.NozzleTypes.name.label('nozzleType'),
        nozzles_models.NozzleSizes.nozzlesSize.label('nozzleSize'),
        models.OperGroups.idCluster,
        models.OperGroups.idNozzleType,
        models.OperGroups.idNozzleSize,
        models.OperGroups.markingDeletion
    ).join(clusters_models.Clusters, clusters_models.Clusters.id == models.OperGroups.idCluster) \
     .join(nozzles_models.NozzleTypes, nozzles_models.NozzleTypes.id == models.OperGroups.idNozzleType) \
     .join(nozzles_models.NozzleSizes, nozzles_models.NozzleSizes.id == models.OperGroups.idNozzleSize) \
     .all()
    return query


def get_printers_list(oper_group, db: Session):
    query = db.query(
        printers_models.Printers.id,
        printers_models.Printers.name
    ).select_from(models.OperGroups) \
     .join(printers_models.Printers).filter(printers_models.Printers.idOperGroups == oper_group.id) \
     .all()
    return query


def add_printer(opergroup_id, printer_id, db: Session):
    printer = db.query(printers_models.Printers).filter(printers_models.Printers.id == printer_id).first()
    if not printer:
        raise HTTPException(status_code=404, detail=configP.get('oper_group', 'oper_group_printer_not_found'))
    else:
        printer.idOperGroups = opergroup_id
        db.commit()

