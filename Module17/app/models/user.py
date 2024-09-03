from Module17.app.backend.db import Base
from sqlalchemy import Column, ForeignKey,Integer, String,Boolean
from sqlalchemy.orm import relationship
# ForeignKey -указатель, позволяет указать на какую-то другую ячейку и произвести взаимосвязь между таблицами

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))