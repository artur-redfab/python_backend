from sqlalchemy import Column, Integer, String, Numeric
from db.database import Base


class Packing(Base):
    __tablename__ = "packing"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    weight = Column(Numeric(2, 5), nullable=False)

