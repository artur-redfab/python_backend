from pydantic import BaseModel


class OperGroupsBase(BaseModel):
    id: int
    name: str
    idCluster: int
    idNozzleType: int
    idNozzleSize: int
    markingDeletion: bool

    class Config:
        orm_mode = True

