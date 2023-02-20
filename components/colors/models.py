from sqlalchemy import Boolean, Column, Integer, String
from db.database import Base


class Color(Base):
    __tablename__ = "colors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    additionalCleaning = Column(Integer)
    # Column(Integer, ForeignKey("user.id"))
    # owner = relationship("User", back_populates="items")
    composite = Column(Boolean())
    colorMaterialHEX = Column(Integer)
    colorPointHEX = Column(Integer)
    markingDeletion = Column(Boolean())


class ColorCreate(Base):
    __tablename__ = "colors"

    pass


# class ColorUpdate(Base):
#     __tablename__ = "colors"
#     pass


class ColorUpdate(Base):
    __tablename__ = "colors"

    name: str
    additionalCleaning: bool

    class Config:
        orm_mode = True

