import hashlib
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from models import schemas, models
from routers.materials import configP


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
    db_user.markingDeletion = True
    db.commit()


def show_user(db: Session, user_id: int):
    db_user = get_user_by_id(db=db, user_id=user_id)
    db_user.markingDeletion = False
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


# методы для работы с моделью Materials
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
    test_query = db.query(models.Materials.name,
                          models.PolymerBases.name.label('polymerBase'),
                          models.Materials.composite,
                          models.Makers.name.label('maker'),
                          models.Materials.density,
                          models.Materials.printingTemp
                          )\
        .join(models.Makers, models.Makers.id == models.Materials.idMaker)\
        .join(models.PolymerBases, models.PolymerBases.id == models.Materials.idPolymerBase)
    if sort.direction == "DESC":
        test_query = test_query.order_by(attr.desc()).offset(sort.offset).limit(sort.limit).all()
    else:
        test_query = test_query.order_by(attr.asc()).offset(sort.offset).limit(sort.limit).all()
    db = test_query
    return db


# методы для работы с моделью Makers
def create_maker(db: Session, maker: schemas.MakerName):
    db_maker = models.Makers(
        name=maker.name
    )
    db.add(db_maker)
    db.commit()
    db.refresh(db_maker)
    return db_maker


def change_maker(db: Session, new_data_maker: schemas.MakerName, maker_id: int):
    db_maker = db.query(models.Makers).filter(models.Makers.id == maker_id).first()
    db_maker.name = new_data_maker.name
    db.commit()


def hide_maker(db: Session, maker_id: int):
    db_maker = db.query(models.Makers).filter(models.Makers.id == maker_id).first()
    db_maker.markingDeletion = True
    db.commit()


def show_maker(db: Session, maker_id: int):
    db_maker = db.query(models.Makers).filter(models.Makers.id == maker_id).first()
    db_maker.markingDeletion = False
    db.commit()


def get_makers(db: Session):
    db_makers = db.query(models.Makers).all()
    return db_makers


def get_maker_by_id(db: Session, maker_id: int):
    db_maker = db.query(models.Makers).filter(models.Makers.id == maker_id).first()
    return db_maker


# методы для работы с моделью vacuumSystem
def create_vacuum_system(db: Session, vs: schemas.VacuumSystemChangeCreate):
    db_vs = models.VacuumSystem(
        name=vs.name,
        ip=vs.ip,
        port=vs.port
    )
    db.add(db_vs)
    db.commit()
    db.refresh(db_vs)
    return db_vs


def change_vacuum_system(db: Session, new_data_vs: schemas.VacuumSystemChangeCreate, vs_id: int):
    db_vs = db.query(models.VacuumSystem).filter(models.VacuumSystem.id == vs_id).first()
    db_vs.name = new_data_vs.name
    db_vs.ip = new_data_vs.ip
    db_vs.port = new_data_vs.port
    db.commit()


def hide_vacuum_system(db: Session, vs_id: int):
    db_vs = db.query(models.VacuumSystem).filter(models.VacuumSystem.id == vs_id).first()
    db_vs.markingDeletion = True
    db.commit()


def show_vacuum_system(db: Session, vs_id: int):
    db_vs = db.query(models.VacuumSystem).filter(models.VacuumSystem.id == vs_id).first()
    db_vs.markingDeletion = False
    db.commit()


def get_list_vacuum_systems(db: Session):
    db_vs = db.query(models.VacuumSystem).all()
    return db_vs


def get_vacuum_system_by_id(db: Session, vs_id: int):
    db_vs = db.query(models.VacuumSystem).filter(models.VacuumSystem.id == vs_id).first()
    return db_vs


