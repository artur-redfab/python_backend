from pydantic import BaseModel


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

