import datetime
import enum

from sqlalchemy import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from db.database import Base
from components.operGroups import models
from components.stands import models
from components.vacuumSystem import models
from components.nozzles import models


class SensorDataType(enum.Enum):
    chamberTemp = int
    chamberTempSet = int
    doorError = bool
    doorStatus = int
    filmbroachError = bool
    filmbroachStatus = bool
    hotend1Temp = int
    hotend1TempSet = int
    hotend2Temp = int
    hotend2TempSet = int
    positionX = int
    positionY = int
    positionZ = int
    rpiTemp = int
    tableTemp = int
    tableTempSet = int
    ventRadiator1 = bool
    ventRadiator2 = bool
    ventZonePrinting = int
    ventZoneRemovalParts = bool


class Sensors(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    nameIdentifer = Column(String, nullable=False)
    idSensorGroup = Column(Integer, ForeignKey('sensorGroups.id'))
    dataType = Column(Enum(SensorDataType), nullable=False)
    description = Column(String, nullable=False)
    requiredUsed = Column(Boolean, nullable=False)
    сanDeactivate = Column(Boolean, nullable=False, default=False)


class SensorsInPrinters(Base):
    __tablename__ = 'sensorsInPrinters'

    id = Column(Integer, primary_key=True, nullable=False)
    idPrinter = Column(Integer, ForeignKey('printers.id'), nullable=False)
    idSensor = Column(Integer, ForeignKey('sensors.id'), nullable=False)
    isUsed = Column(Boolean, nullable=False)


class SensorData(Base):
    __tablename__ = 'sensorData'

    id = Column(Integer, primary_key=True, nullable=False)
    period = Column(DateTime, nullable=False, default=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3), name='MSK')))
    idPrinter = Column(Integer, ForeignKey('printers.id'), nullable=False)
    idSensor = Column(Integer, ForeignKey('sensors.id'), nullable=False)
    dataType = Column(Enum(SensorDataType), nullable=False)
    data = Column(String, nullable=False)


class SensorsGroups(Base):
    __tablename__ = 'sensorsGroups'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

