from sqlalchemy import Boolean, Column, Integer, String
from db.database import Base


class VacuumSystem(Base):
    __tablename__ = "vacuumSystem"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip = Column(String)
    port = Column(Integer)
    markingDeletion = Column(Boolean, default=False)

