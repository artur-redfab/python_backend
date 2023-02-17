from datetime import datetime
from pydantic import BaseModel, Field


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
    def __init__(__pydantic_self__, **data: Any):
        super().__init__(data)
        __pydantic_self__.composite = None
        __pydantic_self__.colorMaterialHEX = None

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


# Схемы для таблицы Makers
class MakerName(BaseModel):
    name: str

    class Config:
        orm_mode = True


# Схемы для таблицы vacuumSystem
class VacuumSystemBase(BaseModel):
    id: str

    class Config:
        orm_mode = True


class VacuumSystemChangeCreate(BaseModel):
    name: str
    ip: str
    port: int


class VacuumSystemFeatures(VacuumSystemBase):
    name: str
    ip: str
    port: int
    markingDeletion: bool


# Схемы для таблицы Makers
class MakerName(BaseModel):
    name: str

    class Config:
        orm_mode = True


class MakerId(BaseModel):
    id: str

    class Config:
        orm_mode = True


class MakerList(MakerId):
    name: str
    markingDeletion: bool

# Схемы для таблицы polumerBases
class PolymerBases(BaseModel):
    name: str

    class Config:
        orm_mode = True


# Схемы для таблицы Materials
class Material(BaseModel):
    name: str
    idPolymerBase: int
    composite: bool
    idMaker: int
    density: int
    printingTemp: int
    maxRadiatorTemp: int
    tableTemp: int
    blowingParts: int
    chamberTemp: int
    timeSwitchCoolingMode: int
    coolingModeTemp: int
    materialUnloadSpeed: int
    materialUnloadTemp: int
    materialUnloadLength: int
    materialLoadSpeed: int
    materialCleanLength: int
    materialServeCoef: int
    gramsCost: int

    class Config:
        orm_mode = True


class MaterialId(BaseModel):
    id: str

    class Config:
        orm_mode = True


class MaterialFeatures(Material):
    id: str
    markingDeletion: bool

    class Config:
        orm_mode = True


class SortProjects(BaseModel):
    limit: int = 10
    offset: int

class SortMaterials(BaseModel):
    limit: int = 0
    offset: int = 0
    sortBy: str = "name"
    direction: str = "ASC"

