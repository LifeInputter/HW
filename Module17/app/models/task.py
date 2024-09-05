from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
# from Module17.app.models.user import User


# ForeignKey -указатель, позволяет указать на какую-то другую ячейку и произвести взаимосвязь между таблицами

class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates='tasks')


from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))




'''
"Модели SQLALchemy. Отношения между таблицами."
Цель: усвоить основные правила структурирования проекта с использованием FastAPI. Научиться создавать модели баз данных, используя SQLAlchemy.

Задача "Модели SQLAlchemy":
Необходимо создать 2 модели для базы данных, используя SQLAlchemy.
База данных и движок:
В модуле db.py:
Импортируйте все необходимые функции и классы , создайте движок указав пусть в БД - 'sqlite:///taskmanager.db' и локальную сессию (по аналогии с видео лекцией).
Создайте базовый класс Base для других моделей, наследуясь от DeclarativeBase.
Модели баз данных:
В модуле task.py создайте модель Task, наследованную от ранее написанного Base со следующими атрибутами:
__tablename__ = 'tasks'
id - целое число, первичный ключ, с индексом.
title - строка.
content - строка.
priority - целое число, по умолчанию 0.
completed - булевое значение, по умолчанию False.
user_id - целое число, внешний ключ на id из таблицы 'users', не NULL, с индексом.
slug - строка, уникальная, с индексом.
user - объект связи с таблицей с таблицей User, где back_populates='tasks'.
В модуле user.py создайте модель User, наследованную от ранее написанного Base со следующими атрибутами:
__tablename__ = 'users'
id - целое число, первичный ключ, с индексом.
username - строка.
firstname - строка.
lastname - строка.
age - целое число.
slug - строка, уникальная, с индексом.
tasks - объект связи с таблицей с таблицей Task, где back_populates='user'.
После описания моделей попробуйте распечатать SQL запрос в консоль при помощи CrateTable (аналогично видео).
Не забудьте об импорте одного класса модели в модуль с другим, чтобы таблицы были видны друг другу.
Для более удобного импорта необходимо дополнить __init__.py в пакете models следующими строками:
from .user import User from .task import Task

Таким образом вы получите 2 модели связанные один(User) ко многим(Task).
'''