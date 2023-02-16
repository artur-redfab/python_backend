from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
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


# Модель Projects

class Projects:
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    idPriority = Column(Integer) # FK!!!!!
    createDate = Column(DateTime, nullable=False)
    deadLine = Column(DateTime, nullable=False)
    changeDate = Column(DateTime)
    orderNumber = Column(String, nullable=False)
    idResponsible = Column(Integer, nullable=False) # FK !!!!!
    idAuthor = Column(Integer, nullable=False) # FK !!!!!!
    comment = Column(String)
    markingDeletion = Column(Boolean, nullable=False, default=False)

