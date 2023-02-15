from pydantic import BaseModel


class ColorBase(BaseModel):
    name: str
    additionalCleaning: str | None = None


class ColorCreate(ColorBase):
    pass


class ColorUpdate(ColorBase):
    name: str | None = None
    additionalCleaning: str | None = None

    class Config:
        orm_mode = True


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


# Схемы для таблицы vacuumSystem
class VacuumSystemBase(BaseModel):
    id: str

    class Config:
        orm_mode = True


class VacuumSystemFeatures(VacuumSystemBase):
    name: str
    ip: str
    port: int
    markingDeletion: bool


class VacuumSystemChangeCreate(BaseModel):
    name: str
    ip: str
    port: int

