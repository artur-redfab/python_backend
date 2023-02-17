from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.materials import schemas, models
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


def create_material(db: Session, material: schemas.Material):
    db_materials = models.Materials(
        name=material.name,
        idPolymerBase=material.idPolymerBase,
        composite=material.composite,
        idMaker=material.idMaker,
        density=material.density,
        printingTemp=material.printingTemp,
        maxRadiatorTemp=material.maxRadiatorTemp,
        tableTemp=material.tableTemp,
        blowingParts=material.blowingParts,
        chamberTemp=material.chamberTemp,
        timeSwitchCoolingMode=material.timeSwitchCoolingMode,
        coolingModeTemp=material.coolingModeTemp,
        materialUnloadSpeed=material.materialUnloadSpeed,
        materialUnloadTemp=material.materialUnloadTemp,
        materialUnloadLength=material.materialUnloadLength,
        materialLoadSpeed=material.materialLoadSpeed,
        materialCleanLength=material.materialCleanLength,
        materialServeCoef=material.materialServeCoef,
        gramsCost=material.gramsCost
    )
    db.add(db_materials)
    db.commit()
    db.refresh(db_materials)
    return db_materials


def get_material_by_id(db: Session, mat_id: int):
    db_material = db.query(models.Materials).filter(models.Materials.id == mat_id).first()
    return db_material


def change_material(db: Session, mat_id: int, new_data_material: schemas.Material):
    db_material = db.query(models.Materials).filter(models.Materials.id == mat_id).first()
    db_material.name = new_data_material.name
    db_material.idPolymerBase = new_data_material.idPolymerBase
    db_material.composite = new_data_material.composite
    db_material.idMaker = new_data_material.idMaker
    db_material.density = new_data_material.density
    db_material.printingTemp = new_data_material.printingTemp
    db_material.maxRadiatorTemp = new_data_material.maxRadiatorTemp
    db_material.tableTemp = new_data_material.tableTemp
    db_material.blowingParts = new_data_material.blowingParts
    db_material.chamberTemp = new_data_material.chamberTemp
    db_material.timeSwitchCoolingMode = new_data_material.timeSwitchCoolingMode
    db_material.coolingModeTemp = new_data_material.coolingModeTemp
    db_material.materialUnloadSpeed = new_data_material.materialUnloadSpeed
    db_material.materialUnloadTemp = new_data_material.materialUnloadTemp
    db_material.materialUnloadLength = new_data_material.materialUnloadLength
    db_material.materialLoadSpeed = new_data_material.materialLoadSpeed
    db_material.materialCleanLength = new_data_material.materialCleanLength
    db_material.materialServeCoef = new_data_material.materialServeCoef
    db_material.gramsCost = new_data_material.gramsCost
    db.commit()


def hide_material(db: Session, mat_id: int):
    db_material = db.query(models.Materials).filter(models.Materials.id == mat_id).first()
    db_material.markingDeletion = True
    db.commit()


def show_material(db: Session, mat_id: int):
    db_material = db.query(models.Materials).filter(models.Materials.id == mat_id).first()
    db_material.markingDeletion = False
    db.commit()


def get_materials(sort: schemas.SortMaterials, db: Session):
    if not hasattr(models.Materials, sort.sortBy):
        return JSONResponse(status_code=400, content=configP.get('materials', 'sort_error'))
    attr = getattr(models.Materials, sort.sortBy)
    db_materials = db.query(models.Materials.name,
                          models.PolymerBases.name.label('polymerBase'),
                          models.Materials.composite,
                          models.Makers.name.label('maker'),
                          models.Materials.density,
                          models.Materials.printingTemp
                          )\
        .join(models.Makers, models.Makers.id == models.Materials.idMaker)\
        .join(models.PolymerBases, models.PolymerBases.id == models.Materials.idPolymerBase)
    if sort.direction == "DESC":
        db_materials = db_materials.order_by(attr.desc()).offset(sort.offset).limit(sort.limit).all()
    else:
        db_materials = db_materials.order_by(attr.asc()).offset(sort.offset).limit(sort.limit).all()
    return db_materials

