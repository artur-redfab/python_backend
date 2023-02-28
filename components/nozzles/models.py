from sqlalchemy import Boolean, Column, Integer, String
from db.database import Base


class NozzleTypes(Base):
    __tablename__ = "nozzleTypes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    compositesPrinting = Column(Boolean, default=False)
    tempIncrease = Column(Integer)


class NozzleSizes(Base):
    __tablename__ = "nozzleSizes"

    id = Column(Integer, primary_key=True, index=True)
    compositesPrinting = Column(Boolean, default=False)
    nozzlesSize = Column(Integer)

