from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class Partners(Base):
    __tablename__ = 'partners'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    inn = Column(String, nullable=True)
    kpp = Column(String)
    address = Column(String)
    comment = Column(String)
    markingDeletion = Column(Boolean, nullable=True, default=False)

