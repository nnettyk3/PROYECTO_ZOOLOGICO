from sqlalchemy import Column, Integer, String
from modelos.base import Base 

class Cuidador(Base):
    __tablename__ = 'cuidadores'

    id_cuidador = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    turno = Column(String(50))
    especialidad = Column(String(100))
