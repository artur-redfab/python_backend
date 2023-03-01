from pydantic import BaseModel


class NozzleTypesBase(BaseModel):
    id: int
    name: str
    tempIncrease: int
    compositesPrinting: bool

    class Config:
        orm_mode = True


class NozzleSizesBase(BaseModel):
    id: int
    nozzlesSize: int
    compositesPrinting: bool

    class Config:
        orm_mode = True

