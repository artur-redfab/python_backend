from sqlalchemy import Column, Integer, String
from db.database import Base


class PolymerBases(Base):
    __tablename__ = "polymerBases"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)

