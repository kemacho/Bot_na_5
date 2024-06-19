# __all__ - публичный список объектов
# https://ru.stackoverflow.com/questions/27983/%D0%A7%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-all-%D0%B2-python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


# Декларативная модель базы данных
# https://metanit.com/python/database/3.2.php

# Как связаны модели
# Юзер: преподаватель и слушатели (User), у каждого слушателя есть преподаватель к которому закреплен (user_teacher_id)
# Фолдер: каждая папка привязана к преподавателю (user_teacher_id)
# Через преподавателя можно получить доступ к его папкам и слушателям (сравнивая айдишники)

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
