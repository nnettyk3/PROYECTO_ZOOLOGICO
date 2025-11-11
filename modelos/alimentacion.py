from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from modelos.base import Base

class Alimentacion(Base):
    __tablename__ = 'alimentacion'

    id_alimentacion = Column(Integer, primary_key=True, autoincrement=True)
    id_animal = Column(Integer, ForeignKey('animal.id_animal'), nullable=False)
    tipo_comida = Column(String(100), nullable=False)
    cantidad = Column(String(50))
    horario = Column(DateTime)
    habilitado = Column(Boolean, default=1, nullable=False)

   