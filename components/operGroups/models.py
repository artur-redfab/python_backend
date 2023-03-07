from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from db.database import Base
from components.clusters import models
from components.nozzles import models


class OperGroups(Base):
    __tablename__ = "operGroups"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String)
    idCluster = Column(Integer, ForeignKey('clusters.id'), nullable=False)
    idNozzleType = Column(Integer, ForeignKey('nozzleTypes.id'), nullable=False)
    idNozzleSize = Column(Integer, ForeignKey('nozzleSizes.id'), nullable=False)
    markingDeletion = Column(Boolean, nullable=False, default=False)

