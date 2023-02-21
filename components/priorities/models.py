from sqlalchemy import Column, Integer, String
from db.database import Base


class Priorities(Base):
    __tablename__ = "priorities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

