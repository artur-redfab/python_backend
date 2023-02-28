from pydantic import BaseModel
from components.sensors.models import SensorDataType


class SortSensors(BaseModel):
    sortBy: str = "name"
    direction: str = "ASC"
    limit: int = 10
    offset: int


class Features(BaseModel):
    id: str
    name: str
    nameIdentifier: str
    idSensorGroup: str
    description: str
    requiredUsed: bool
    canDeactivate: bool

    class Config:
        orm_mode = True


class Sensor(Features):
    dataType: SensorDataType


class Groups(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True

