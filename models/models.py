from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from .database import Base


class Color(Base):
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    additionalCleaning = Column(Integer)
    # Column(Integer, ForeignKey("user.id"))
    # owner = relationship("User", back_populates="items")
    composite = Column(Boolean())
    colorMaterialRGB = Column(Integer)
    colorPointRGB = Column(Integer)
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


# Модель Users
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    firstname = Column(String)
    idRole = Column(Integer, ForeignKey("roles.id"))
    position = Column(String)
    login = Column(String)
    passwordHash = Column(String)
    markingDeletion = Column(Boolean, default=False)


class Roles(Base):
    __tablename__ ="roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Materials(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    idPolymerBase = Column(Integer, ForeignKey("polymerBases.id"), nullable=False)
    composite = Column(Boolean, nullable=False)
    idMaker = Column(Integer, ForeignKey("makers.id"), nullable=False)
    density = Column(Numeric, nullable=False)
    printingTemp = Column(Integer, nullable=False)
    maxRadiatorTemp = Column(Integer, nullable=False)
    tableTemp = Column(Integer, nullable=False)
    blowingParts = Column(Integer, nullable=False)
    chamberTemp = Column(Integer, nullable=False)
    timeSwitchCoolingMode = Column(Integer, nullable=False)
    coolingModeTemp = Column(Integer, nullable=False)
    materialUnloadSpeed = Column(Integer, nullable=False)
    materialUnloadTemp = Column(Integer, nullable=False)
    materialUnloadLength = Column(Integer, nullable=False)
    materialLoadSpeed = Column(Integer, nullable=False)
    materialCleanLength = Column(Integer, nullable=False)
    materialServeCoef = Column(Integer, nullable=False)
    gramsCost = Column(Numeric)
    markingDeletion = Column(Boolean, default=False)

