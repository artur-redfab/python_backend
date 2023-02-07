from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

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


class ColorUpdate(Base):
    __tablename__ = "colors"
    pass


# Модель Users
# - Нет понимания корректой инициализации полей модели
# - Что делать с хэш-паролем
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    firstname = Column(String)
    # Связано с таблицей roles. Будет ли это внешний ключ?
    idRole = Column(String)
    position = Column(String)
    login = Column(String)
    passwordHash = Column(String)
    markingDeletion = Column(Boolean, default=False)
gi
