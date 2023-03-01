from pydantic import BaseModel


class StandsBase(BaseModel):
    id: int
    name: str
    idCluster: int
    markingDeletion: bool

    class Config:
        orm_mode = True

