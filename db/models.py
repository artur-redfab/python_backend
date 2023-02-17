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


# Модель polymerBases
class PolymerBases(Base):
    __tablename__ = "polymerBases"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)


class VacuumSystem(Base):
    __tablename__ = "vacuumSystem"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip = Column(String)
    port = Column(Integer)
    markingDeletion = Column(Boolean, default=False)

