from sqlalchemy import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db.database import Base


class Stands(Base):
    __tablename__ = "stands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    markingDeletion = Column(Boolean, nullable=False, default=False)
    idCluster = Column(Integer, nullable=False)
