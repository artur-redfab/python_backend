from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.partners import models, schemas
from components.materials.routers import configP


def get_partner_by_id(db: Session, id: int):
    partner = db.query(models.Partners).filter(models.Partners.id == id).first()
    return partner


def create_partner(db: Session, partner: schemas.CreateChangePartner):
    new_partner = models.Partners(
        name=partner.name,
        inn=partner.inn,
        kpp=partner.kpp,
        address=partner.address,
        comment=partner.comment
    )
    db.add(new_partner)
    db.commit()
    db.refresh(new_partner)
    return get_partner_by_id(db=db, id=new_partner.id)


def change_partner(db: Session, partner: schemas.CreateChangePartner, partner_id: int):
    db_partner = get_partner_by_id(db=db, id=partner_id)
    db_partner.name = partner.name
    db_partner.inn = partner.inn
    db_partner.kpp = partner.kpp
    db_partner.address = partner.address
    db_partner.comment = partner.comment
    db.commit()


def hide_partner(db: Session, partner):
    partner.markingDeletion = True
    db.commit()


def show_partner(db: Session, partner):
    partner.markingDeletion = False
    db.commit()


def get_projects(db: Session, sort: schemas.SortPartners):
    if not hasattr(models.Partners, sort.sortBy):
        return JSONResponse(status_code=200, content=configP.get('partners', 'sort_error'))
    attr = getattr(models.Partners, sort.sortBy)
    db_query = db.query(models.Partners)
    if sort.direction == "DESC":
        db_query = db_query.order_by(attr.desc())
    else:
        db_query = db_query.order_by(attr.asc())
    db_query = db_query.offset(sort.offset).limit(sort.limit).all()
    return db_query

