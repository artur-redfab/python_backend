from pydantic import BaseModel


class PackingBase(BaseModel):
    id: str
    name: str
    weight: float
    markingDeletion: bool

