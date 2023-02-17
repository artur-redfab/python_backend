from sqlalchemy.orm import Session
from components.makers import schemas, models


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

