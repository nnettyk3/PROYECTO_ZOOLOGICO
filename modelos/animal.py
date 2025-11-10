

class Animal:
    def __init__(self, id_animal, nombre, especie, edad, habitat):
        # Atributos coinciden con las columnas de la tabla 'animal'
        self.id_animal = id_animal
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def __str__(self):
        """Representación legible del objeto."""
        return f"Animal(ID: {self.id_animal}, Nombre: {self.nombre}, Especie: {self.especie}, Hábitat: {self.habitat}, Edad: {self.edad})"

    def to_dict(self):
        """Convierte el objeto a un diccionario (útil para la IU o BBDD)."""
        return {
            'id_animal': self.id_animal,
            'nombre': self.nombre,
            'especie': self.especie,
            'edad': self.edad,
            'habitat': self.habitat
        }