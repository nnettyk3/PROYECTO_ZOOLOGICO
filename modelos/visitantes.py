from sqlalchemy import Column, Integer, String, Boolean
from modelos.base import Base 

class Visitante(Base):
    __tablename__ = 'visitantes'

    id_visitante = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    rut = Column(String(12), unique=True)
    habilitado = Column(Boolean, default=1, nullable=False) 

    