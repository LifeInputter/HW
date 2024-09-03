from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

# создаем engine для связи с БД
engine = create_engine("sqlite:///taskmanager.db", echo=True)

# создаем сессию связи с БД
SessionLocal = sessionmaker(bind=engine)


# создаем класс будуще БД
class Base(DeclarativeBase):
    pass
