import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Interval, DateTime, Numeric
from components.tasks.models import Tasks
from components.users.models import Users
from db.database import Base


class TaskFiles(Base):
    __tablename__ = "taskFiles"

    id = Column(Integer, primary_key=True, index=True)
    nameFile = Column(String, nullable=False)
    extFile = Column(String, nullable=False)
    idTask = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    idOwner = Column(Integer, ForeignKey('users.id'), nullable=False)
    sizeFile = Column(Numeric, nullable=False)
    hashFile = Column(String, nullable=False)
    path = Column(String, nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3), name='MSK')))


