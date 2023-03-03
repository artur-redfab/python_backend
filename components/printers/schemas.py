from datetime import datetime
from pydantic import BaseModel


class CreatePrinter(BaseModel):
    name: str
    idStand: int
    idOperGroups: int
    idModulePlace: int
    idVacuumSystem: int
    vacuumSystemValue: str
    serialNumber: str
    printerIP: str
    printerPort: int
    selectiveSystemIP: str
    selectiveSystemPort: int
    idTableType: int
    basicCellQuantity: int
    supportCellQuantity: int
    activeBasicCell: int
    activeSupportCell: int
    webIs: bool
    webcamURL: str
    inPrintQueue: bool
    markingDeletion: bool = False

    class Config:
        orm_mode = True


class CreatedPrinter(BaseModel):
    id: int
    name: str
    idStand: int
    idOperGroups: int
    idModulePlace: int
    idVacuumSystem: int
    vacuumSystemValue: str
    serialNumber: str
    printerIP: str
    printerPort: int
    selectiveSystemIP: str
    selectiveSystemPort: int
    idTableType: int
    basicCellQuantity: int
    supportCellQuantity: int
    activeBasicCell: int
    activeSupportCell: int
    webIs: bool
    webcamURL: str
    comment: str
    inPrintQueue: bool
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

