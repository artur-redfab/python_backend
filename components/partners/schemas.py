from pydantic import BaseModel


class CreateChangePartner(BaseModel):
    name: str
    inn: str
    kpp: str
    address: str
    comment: str


class IdPartner(BaseModel):
    id: str

    class Config:
        orm_mode = True


class SortPartners(BaseModel):
    sortBy: str = "name"
    direction: str = "ASC"
    limit: int = 10
    offset: int


class ListPartners(IdPartner, CreateChangePartner):
    markingDeletion: bool


