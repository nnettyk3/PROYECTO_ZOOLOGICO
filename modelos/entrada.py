
# Módulo: modelos/entrada.py

class Entrada:
    def __init__(self, id_entrada, tipo_entrada, precio, fecha_compra):
        self.id_entrada = id_entrada
        self.tipo_entrada = tipo_entrada # Ej: 'Adulto', 'Niño', 'Familiar'
        self.precio = precio
        self.fecha_compra = fecha_compra # Usaremos strings o datetime objects

    def __str__(self):
        return f"Entrada(ID: {self.id_entrada}, Tipo: {self.tipo_entrada}, Precio: {self.precio})"