from sqlalchemy import Column, Integer, String
from modelos.base import Base

class Animal(Base):
    __tablename__ = 'animal'

    id_animal = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    especie = Column(String(100), nullable=False)
    edad = Column(Integer)
    habitat = Column(String(100))  