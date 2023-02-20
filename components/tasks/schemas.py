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

