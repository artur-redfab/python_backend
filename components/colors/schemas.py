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


