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


def set_color(db: Session, id: int):
    db_color = db.query(models.Color).filter(models.Color.id == id).first()
    db_color.update({'name': '12345'})
    db.commit()
    # db.refresh(db_color)
    return db_color


def get_features(id:int, db: Session):
    return db.query(models.Color).filter(models.Color.id == id).first()
