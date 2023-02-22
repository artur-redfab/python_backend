import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Interval, DateTime, Numeric
from db.database import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    idProject = Column(Integer, ForeignKey('projects.id'), nullable=False)
    idPriority = Column(Integer, ForeignKey('priorities.id'), nullable=False)
    numberCopies = Column(Integer, nullable=False)
    planPrintTime = Column(Interval, nullable=False)
    factPrintTime = Column(Interval)
    idOperGroup = Column(Integer, nullable=False) # TODO: ForeignKey(""), nullable=False)
    twoExtrPrint = Column(Boolean, nullable=False)
    idBasicMaterial = Column(Integer, ForeignKey('materials.id'), nullable=False)
    idBasicColor = Column(Integer, ForeignKey('colors.id'), nullable=False)
    idSupportMaterial = Column(Integer, ForeignKey('materials.id'), nullable=False)
    idSupportColor = Column(Integer, ForeignKey('colors.id'), nullable=False)
    volume = Column(Numeric, nullable=False)
    markingDeletion = Column(Boolean, nullable=False, default=False)
    update = Column(DateTime, nullable=False, default=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3), name='MSK')))


class TaskStatuses(Base):
    __tablename__ = "taskStatuses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class TaskStatusHistory(Base):
    __tablename__ = "taskStatusHistory"

    id = Column(Integer, primary_key=True, index=True)
    period = Column(DateTime, nullable=False, default=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3), name='MSK')))
    idTask = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    idTaskStatus = Column(Integer, ForeignKey('taskStatuses.id'), nullable=False)


class TasksCopies(Base):
    __tablename__ = "tasksCopies"

    id = Column(Integer, primary_key=True, index=True)
    idTask = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    numCopy = Column(Integer, nullable=False)
    printTime = Column(Integer, nullable=False)
    startAt = Column(DateTime)
    idTaskStatus = Column(Integer, ForeignKey('taskStatuses.id'))
    markingDeletion = Column(Boolean, nullable=False, default=False)

