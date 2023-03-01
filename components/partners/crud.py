from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from components.partners import models, schemas



def get_partner_by_id(db: Session, id: int):
    partner = db.query(models.Partners).filter(models.Partners.id == id).first()
    return partner


def create_partner(db: Session, partner: schemas.CreatePartner):
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

