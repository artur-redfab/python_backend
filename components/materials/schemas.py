from datetime import datetime
from pydantic import BaseModel, Field


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
    sortBy: str = "name"
    direction: str = "ASC"

