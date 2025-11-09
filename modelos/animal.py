

class Animal:
    def __init__(self, id_animal, nombre, especie, edad, habitat):
        self.id_animal = id_animal
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {self.habitat}"
