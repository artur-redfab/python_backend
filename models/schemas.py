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


class SortMaterials(BaseModel):
    limit: int = 0
    offset: int = 0
    sortBy: str = "string"
    direction: str = "ASC"


class SortedMaterials(BaseModel):
    name: str
    polymer: PolymerBases
    composite: bool
    maker: MakerName
    density: int
    printingTemp: int

    class Config:
        orm_mode = True









