

class Cuidador:
    def __init__(self, id_cuidador, nombre, turno, especialidad):
        self.id_cuidador = id_cuidador
        self.nombre = nombre
        self.turno = turno
        self.especialidad = especialidad
        # Lista para almacenar los animales asignados a este cuidador
        self.animales_asignados = []

    def __str__(self):
        return f"Cuidador(ID: {self.id_cuidador}, Nombre: {self.nombre}, Turno: {self.turno}, Especialidad: {self.especialidad})"

    def to_dict(self):
        return {
            'id_cuidador': self.id_cuidador,
            'nombre': self.nombre,
            'turno': self.turno,
            'especialidad': self.especialidad
        }