from sqlalchemy import Column, Integer, ForeignKey, Date, String, Text
from modelos.base import Base 

class CuidadoMedico(Base):
    __tablename__ = 'cuidados_medicos'

    id_cuidado_medico = Column(Integer, primary_key=True, autoincrement=True)
    id_animal = Column(Integer, ForeignKey('animal.id_animal'), nullable=False)
    fecha = Column(Date, nullable=False)
    tipo_cuidado = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=False)
    veterinario = Column(String(100), nullable=False)
    observaciones = Column(Text)
