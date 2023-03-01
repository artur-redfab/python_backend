import datetime
from sqlalchemy import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db.database import Base
from components.operGroups import models
from components.stands import models
from components.vacuumSystem import models
from components.nozzles import models


class Printers(Base):
    __tablename__ = "printers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    idStand = Column(Integer, ForeignKey('stands.id'))
    idOperGroups = Column(Integer, ForeignKey('operGroups.id'))
    idModulePlace = Column(Integer, ForeignKey('modulePlaces.id'), nullable=False)
    idVacuumSystem = Column(Integer, ForeignKey('vacuumSystem.id'), nullable=False)
    vacuumSystemValue = Column(String, nullable=False)
    serialNumber = Column(String, nullable=False)
    printerIP = Column(String, nullable=False)
    printerPort = Column(Integer, nullable=False)
    selectiveSystemIP = Column(String, nullable=False)
    selectiveSystemPort = Column(Integer, nullable=False)
    idTableType = Column(Integer, ForeignKey('tableTypes.id'), nullable=False)
    basicCellQuantity = Column(Integer, nullable=False)
    supportCellQuantity = Column(Integer, nullable=False)
    activeBasicCell = Column(Integer, nullable=False)
    activeSupportCell = Column(Integer, nullable=False)
    webIs = Column(Boolean, nullable=False, default=False)
    webcamURL = Column(String, nullable=False)
    inPrintQueue = Column(Boolean, nullable=False, default=False)
    markingDeletion = Column(Boolean, nullable=False, default=False)


class TableTypes(Base):
    __tablename__ = "tableTypes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    conveyorPrinting = Column(Boolean, nullable=False)
    stretchingLength = Column(Integer, nullable=False)
    tempIncrease = Column(Integer, nullable=False)
    markingDeletion = Column(Boolean, nullable=False, default=False)


class ModulePlaces(Base):
    __tablename__ = "modulePlaces"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

