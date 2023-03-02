from pydantic import BaseModel


class NozzleTypesBase(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class NozzleTypesFeatures(NozzleTypesBase):
    tempIncrease: int
    compositesPrinting: bool


class NozzleSizesBase(BaseModel):
    id: int
    nozzlesSize: int
    compositesPrinting: bool

    class Config:
        orm_mode = True

