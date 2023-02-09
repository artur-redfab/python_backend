import hashlib
from sqlalchemy.orm import Session
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
    db_vs.markingDelete = True
    db.commit()


def show_vacuum_system(db: Session, vs_id: int):
    db_vs = db.query(models.VacuumSystem).filter(models.VacuumSystem.id == vs_id).first()
    db_vs.markingDelete = False
    db.commit()


def get_list_vacuum_systems(db: Session):
    db_vs = db.query(models.VacuumSystem).order_by(models.VacuumSystem.id).all()
    return db_vs


def get_features_vacuum_system_by_id(db: Session, vs_id: int):
    db_vs = db.query(models.VacuumSystem).filtre(models.VacuumSystem.id == vs_id).first()
    return db_vs

