from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.printers import schemas, models

from components.vacuumSystem import models as vacuum_system_models
# from components.users import models as users_models
# from components.projects import schemas, models
# from components.materials.routers import configP


def create_printer(db: Session, printer: schemas.CreatePrinter):
    db_printer = models.Printers(
        name=printer.name,
        idStand=printer.idStand,
        idOperGroups=printer.idOperGroups,
        idModulePlace=printer.idModulePlace,
        idVacuumSystem=printer.idVacuumSystem,
        vacuumSystemValue=printer.vacuumSystemValue,
        serialNumber=printer.serialNumber,
        printerIP=printer.printerIP,
        printerPort=printer.printerPort,
        selectiveSystemIP=printer.selectiveSystemIP,
        selectiveSystemPort=printer.selectiveSystemPort,
        idTableType=printer.idTableType,
        basicCellQuantity=printer.basicCellQuantity,
        supportCellQuantity=printer.supportCellQuantity,
        activeBasicCell=printer.activeBasicCell,
        activeSupportCell=printer.activeSupportCell,
        webIs=printer.webIs,
        webcamURL=printer.webcamURL,
        inPrintQueue=printer.inPrintQueue,
        markingDeletion=printer.markingDeletion,
    )
    db.add(db_printer)
    db.commit()
    db.refresh(db_printer)
    query = get_printer_features(db=db, printer_id=db_printer.id)
    return query


def get_printer_by_id(printer_id: int, db: Session):
    db_printer = db.query(models.Printers).filter(models.Printers.id == printer_id).first()
    return db_printer


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


# name = printer.name,
# idStand = printer.idStand,
# idOperGroups = printer.idOperGroups,
# idModulePlace = printer.idModulePlace,
# idVacuumSystem = printer.idVacuumSystem,
# vacuumSystemValue = printer.vacuumSystemValue,
# serialNumber = printer.serialNumber,
# printerIP = printer.printerIP,
# printerPort = printer.printerPort,
# selectiveSystemIP = printer.selectiveSystemIP,
# selectiveSystemPort = printer.selectiveSystemPort,
# idTableType = printer.idTableType,
# basicCellQuantity = printer.basicCellQuantity,
# supportCellQuantity = printer.supportCellQuantity,
# activeBasicCell = printer.activeBasicCell,
# activeSupportCell = printer.activeSupportCell,
# webIs = printer.webIs,
# webcamURL = printer.webcamURL,
# inPrintQueue = printer.inPrintQueue,
# markingDeletion = printer.markingDeletion,

def get_printer_features(printer_id: int, db: Session):
    query = db.query(
        models.Printers.id,
        models.Printers.name,
        models.Printers.idStand,
        models.Printers.idOperGroups,
        models.Printers.idModulePlace,
        models.Printers.idVacuumSystem,
        models.Printers.vacuumSystemValue,
        models.Printers.serialNumber,
        models.Printers.printerIP,
        models.Printers.printerPort,
        models.Printers.selectiveSystemIP,
        models.Printers.selectiveSystemPort,
        models.Printers.idTableType,
        models.Printers.basicCellQuantity,
        models.Printers.supportCellQuantity,
        models.Printers.activeBasicCell,
        models.Printers.activeSupportCell,
        models.Printers.webIs,
        models.Printers.webcamURL,
        models.Printers.inPrintQueue,
        # models.ProjectStatusHistory.idProjectStatus # TODO!!!!
        models.Printers.markingDeletion
    ).join(vacuum_system_models.VacuumSystem, vacuum_system_models.VacuumSystem.id == models.Printers.idVacuumSystem) \
        .filter(models.Printers.id == printer_id).first()
    return query
