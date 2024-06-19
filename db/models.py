from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, index=True, primary_key=True)
    user_teacher_id = Column(Integer, nullable=True)
    token = Column(String, nullable=True)
    name = Column(String)


class YandexDiskFolder(Base):
    __tablename__ = 'yandex_disk_folders'
    id = Column(Integer, index=True, primary_key=True)
    user_teacher_id = Column(Integer)
    name = Column(String)
    date = Column(String, nullable=True)
