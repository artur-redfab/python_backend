from pydantic import BaseModel


class ColorBase(BaseModel):
    name: str
    additionalCleaning: str | None = None


class ColorCreate(ColorBase):
    pass


class ColorUpdate(BaseModel):
    name: str | None = None
    additionalCleaning: str | None = None


class Color(ColorBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Схемы для таблицы Users
class UserBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    firstname: str
    login: str
    password: str
    idRole: str
    position: str

    class Config:
        orm_mode = True


class UserShowHide(BaseModel):
    markingDeletion: bool








