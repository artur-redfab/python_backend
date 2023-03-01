from pydantic import BaseModel


class CreatePartner(BaseModel):
    name: str
    inn: str
    kpp: str
    address: str
    comment: str


class IdPartner(BaseModel):
    id: str

    class Config:
        orm_mode = True
