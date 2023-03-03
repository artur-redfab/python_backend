from pydantic import BaseModel


class IdOperGroup(BaseModel):
    id: str

    class Config:
        orm_mode = True


class CreateChangeOperGroup(BaseModel):
    name: str
    idCluster: int
    idNozzleType: int
    idNozzleSize: int

    class Config:
        orm_mode = True


class OperGroupsBase(BaseModel):
    id: int
    name: str
    idCluster: int
    idNozzleType: int
    idNozzleSize: int
    markingDeletion: bool

    class Config:
        orm_mode = True


class OperGroupList(IdOperGroup):
    name: str
    cluster: str
    nozzleType: str
    nozzleSize: str
    idCluster: str
    idNozzleType: str
    idNozzleSize: str
    markingDeletion: bool


