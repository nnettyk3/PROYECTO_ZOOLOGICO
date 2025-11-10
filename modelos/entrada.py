from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from modelos.base import Base 

class Entrada(Base):
    __tablename__ = 'entrada'

    id_entrada = Column(Integer, primary_key=True, autoincrement=True)
    fecha_visita = Column(Date, nullable=False)
    precio = Column(Float, nullable=False)
    id_visitante = Column(Integer, ForeignKey('visitantes.id_visitante'))

