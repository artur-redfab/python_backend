from sqlalchemy.orm import Session
from components.vacuumSystem import models, schemas


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

