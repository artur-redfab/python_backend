from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from db.database import Base
from sqlalchemy.orm import relationship


class Materials(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    idPolymerBase = Column(Integer, ForeignKey("polymerBases.id"), nullable=False)
    composite = Column(Boolean, nullable=False)
    idMaker = Column(Integer, ForeignKey("makers.id"), nullable=False)
    density = Column(Numeric, nullable=False)
    printingTemp = Column(Integer, nullable=False)
    maxRadiatorTemp = Column(Integer, nullable=False)
    tableTemp = Column(Integer, nullable=False)
    blowingParts = Column(Integer, nullable=False)
    chamberTemp = Column(Integer, nullable=False)
    timeSwitchCoolingMode = Column(Integer, nullable=False)
    coolingModeTemp = Column(Integer, nullable=False)
    materialUnloadSpeed = Column(Integer, nullable=False)
    materialUnloadTemp = Column(Integer, nullable=False)
    materialUnloadLength = Column(Integer, nullable=False)
    materialLoadSpeed = Column(Integer, nullable=False)
    materialCleanLength = Column(Integer, nullable=False)
    materialServeCoef = Column(Integer, nullable=False)
    gramsCost = Column(Numeric)
    markingDeletion = Column(Boolean, default=False)

    polymer = relationship("PolymerBases", innerjoin=True)
    maker = relationship("Makers", innerjoin=True)

