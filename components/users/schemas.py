from pydantic import BaseModel


class UserBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    firstname: str
    login: str
    password: str
    idRole: int
    position: str

    class Config:
        orm_mode = True


class UserShowHide(BaseModel):
    markingDeletion: bool


class UserFeatures(BaseModel):
    id: str
    name: str
    firstname: str
    login: str
    idRole: int
    position: str
    markingDeletion: bool

