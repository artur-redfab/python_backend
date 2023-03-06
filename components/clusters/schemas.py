from pydantic import BaseModel, Field
from components.stands import schemas


class CreateChangeCluster(BaseModel):
    name: str

    class Config:
        orm_mode = True


class FeaturesCluster(BaseModel):
    name: str
    markingDeletion: bool

    class Config:
        orm_mode = True


class Cluster(FeaturesCluster):
    id: str


class PrintersForStands(BaseModel):
    printerIP: str = Field(alias="ip")
    printerPort: str = Field(alias="port")
    name: str
    id: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class StandsForClusters(BaseModel):
    name: str
    id: str
    printers: list[PrintersForStands]

    class Config:
        orm_mode = True


class AllDataClusters(BaseModel):
    name: str
    id: str
    stands: list[StandsForClusters]

    class Config:
        orm_mode = True

