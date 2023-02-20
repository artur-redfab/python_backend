import hashlib
from sqlalchemy.orm import Session
from components.users import schemas, models


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

