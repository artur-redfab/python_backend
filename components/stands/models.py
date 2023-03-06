from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Stands(Base):
    __tablename__ = "stands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    markingDeletion = Column(Boolean, nullable=False, default=False)
    idCluster = Column(Integer, ForeignKey('clusters.id'), nullable=False)

    printers = relationship("Printers", innerjoin=True)

