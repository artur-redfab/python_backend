from sqlalchemy import Boolean, Column, Integer, String
from db.database import Base


class Makers(Base):
    __tablename__ = "makers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    markingDeletion = Column(Boolean, default=False)

