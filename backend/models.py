#models.py

from sqlalchemy import Column, Integer,String

from database import Base


class User(Base):
    __tablename__ = 'users'
    # columnas de mi base de datos
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True, unique=True)
    password = Column(String(30), index=True) 

