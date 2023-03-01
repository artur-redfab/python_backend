import datetime
import enum

from sqlalchemy import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from db.database import Base


class SensorDataType(enum.Enum):
    boolean = "boolean"
    string = "string"
    int = "int"


class Sensors(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    nameIdentifier = Column(String, nullable=False)
    idSensorGroup = Column(Integer, ForeignKey('sensorGroups.id'))
    dataType = Column(Enum(SensorDataType), nullable=False)
    description = Column(String, nullable=False)
    requiredUsed = Column(Boolean, nullable=False)
    canDeactivate = Column(Boolean, nullable=False, default=False)


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

