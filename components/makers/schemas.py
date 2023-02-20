from pydantic import BaseModel


class MakerName(BaseModel):
    name: str

    class Config:
        orm_mode = True


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



