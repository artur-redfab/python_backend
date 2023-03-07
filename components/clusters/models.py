from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class Clusters(Base):
    __tablename__ = "clusters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    markingDeletion = Column(Boolean, default=False)

    stands = relationship("Stands", innerjoin=True)

