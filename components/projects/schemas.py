from datetime import datetime
from pydantic import BaseModel


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


class SortProjects(BaseModel):
    sortBy: str = "name"
    direction: str = "ASC"
    limit: int = 10
    offset: int


class TasksList(BaseModel):
    id: str
    name: str
    numberCopies: int
    operGroup: str | None
    basicMaterial: str
    basicColorHEX: str
    nozzleType: str | None
    nozzleSize: str | None
    planPrintTime: int
    factPrintTime: int
    volume: int
    markingDeletion: bool

