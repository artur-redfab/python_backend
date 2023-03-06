import datetime

from pydantic import BaseModel


class IdTask(BaseModel):
    id: str

    class Config:
        orm_mode = True


class CreatingChangingTask(BaseModel):
    name: str
    idProject: str = "1"
    idPriority: str = "1"
    numberCopies: int = 1
    planPrintTime: str = "03:00:00"
    twoExtrPrint: bool
    idBasicMaterial: str = "1"
    idSupportMaterial: str = "1"
    idBasicColor: str = "1"
    idSupportColor: str = "1"
    idOperGroup: str = "1"
    volume: int = 3

    class Config:
        orm_mode = True


class Task(CreatingChangingTask, IdTask):
    project: str
    factPrintTime: int | None
    planPrintTime: datetime.timedelta
    basicMaterial: str
    basicColor: str
    supportMaterial: str
    supportColor: str
    idNozzleType: str
    nozzleType: str
    idNozzleSize: str
    nozzleSize: str
    operGroup: str
    idFile: str
    nameFile: str
    extFile: str
    sizeFile: int
    hashFile: str
    markingDeletion: bool

    class Config:
        orm_mode = True


class IdTask(BaseModel):
    id: str

    class Config:
        orm_mode = True


class IdTaskStatus(BaseModel):
    idTaskStatus: str


class TasksList(BaseModel):
    id: str
    name: str
    numberCopies: int
    operGroup: str
    basicMaterial: str
    basicColorHEX: str
    nozzleType: str
    nozzleSize: str | None
    planPrintTime: datetime.timedelta
    factPrintTime: int | None
    volume: int
    markingDeletion: bool

    class Config:
        orm_mode = True

