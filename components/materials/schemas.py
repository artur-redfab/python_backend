from datetime import datetime
from pydantic import BaseModel, Field


class IdTask(BaseModel):
    id: str

    class Config:
        orm_mode = True


class CreatingChangingTask(BaseModel):
    name: str
    idProject: str
    idPriority: str
    numberCopies: int
    planPrintTime: int
    twoExtrPrint: bool
    idBasicMaterial: str
    idSupportMaterial: str
    idBasicColor: str
    idSupportColor: str
    idOperGroup: str
    volume: int

    class Config:
        orm_mode = True


class Task(CreatingChangingTask, IdTask):
    project: str
    factPrintTime: int | None
    basicMaterial: str
    basicColor: str
    supportMaterial: str
    supportColor: str
    idNozzleType: str | None
    nozzleType: str
    idNozzleSize: str | None
    nozzleSize: str | None
    operGroup: str | None
    idFile: str | None
    nameFile: str | None
    extFile: str | None
    sizeFile: int | None
    hashFile: str | None
    markingDeletion: bool


class IdTask(BaseModel):
    id: str

    class Config:
        orm_mode = True

