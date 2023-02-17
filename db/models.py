import datetime
from sqlalchemy import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from .database import Base
from sqlalchemy.orm import relationship


# Модель Projects
class Projects(Base):
    __tablename__ = "projects"

    tz = datetime.timezone(datetime.timedelta(hours=3), name='MSK')
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    idPriority = Column(Integer, ForeignKey('priorities.id'), nullable=False) # FK!!!!!
    createDate = Column(DateTime, nullable=False, default=datetime.datetime.now(tz=tz))
    deadLine = Column(DateTime, nullable=False)
    changeDate = Column(DateTime)
    orderNumber = Column(String, nullable=False)
    idPartner = Column(Integer) #, ForeignKey('partners.id'), nullable=False)
    idResponsible = Column(Integer, ForeignKey('users.id'), nullable=False)
    idAuthor = Column(Integer, ForeignKey('users.id'), nullable=False)
    comment = Column(String)
    markingDeletion = Column(Boolean, nullable=False, default=False)


class Priorities(Base):
    __tablename__ = "priorities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


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


# Модель polymerBases
class PolymerBases(Base):
    __tablename__ = "polymerBases"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)


# модель Makers
class Makers(Base):
    __tablename__ = "makers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    markingDeletion = Column(Boolean, default=False)


class VacuumSystem(Base):
    __tablename__ = "vacuumSystem"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip = Column(String)
    port = Column(Integer)
    markingDeletion = Column(Boolean, default=False)

