from datetime import datetime
from pydantic import BaseModel


class ColorBase(BaseModel):
    name: str
    additionalCleaning: str | None = None


class ColorCreate(ColorBase):
    pass


class ColorUpdate(ColorBase):
    name: str | None = None
    additionalCleaning: str | None = None

    class Config:
        orm_mode = True


class Color(ColorBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Схемы для таблицы Users
class UserBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    firstname: str
    login: str
    password: str
    idRole: int
    position: str

    class Config:
        orm_mode = True


class UserShowHide(BaseModel):
    markingDeletion: bool


class UserFeatures(BaseModel):
    id: str
    name: str
    firstname: str
    login: str
    idRole: int
    position: str
    markingDeletion: bool


#Схемы для таблицы projects

class CreateProject(BaseModel):
    name: str
    idPriority: str = "1"
    deadLine: str = "2023-02-16"
    orderNumber: str
    idPartner: str = "1"
    idResponsible: str = "5"
    idAuthor: str = "5"
    comment: str

    class Config:
        orm_mode = True


class CreatedProject(BaseModel):
    id: str
    name: str
    idPriority: str
    createDate: datetime
    deadLine: datetime
    changeDate: datetime | None
    orderNumber: str
    idPartner: str
    idResponsible: str
    author: str
    idProjectStatus: str | None
    comment: str
    markingDeletion: bool

    class Config:
        orm_mode = True


class ChangeProject(BaseModel):
    name: str
    idPriority: str = "1"
    deadLine: str = "2023-02-1"
    orderNumber: str = "1"
    idPartner: str = "1"
    idResponsible: str = "5"
    comment: str


class ListProjects(BaseModel):
    id: str
    name: str
    idPriority: str
    createDate: str | None
    orderNumber: str
    idPartner: str
    partner: str | None
    idResponsible: str
    responsible: str
    markingDeletion: bool

    class Config:
        orm_mode = True


class SortProjects(BaseModel):
    limit: int = 10
    offset: int
    sortBy: str = "name"
    direction: str = "ASC"

