

class animal:
    def __unit__(self, id_animal, nombre, especie, edad, peso):
        self.id_animal = id_animal
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

        def __str__(self):
            return f"Animal[ID: {self.id_animal}, Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Peso: {self.peso}]"
        
        def alimentar(self, cantidad_comida):
            return f"Alimentado {self.nombre} con {cantidad.cantidad_comida} kg de comida."
        def mover(self, nueva_ubicacion):
            return f"{self.nombre} se ha movido a {nueva_ubicacion}."
        def dormir(self, horas):
            return f"{self.nombre} ha dormido por {horas} horas."
        def hacer_sonido(self):
            return f"{self.nombre} hace un sonido caracteristicas de su especie."
        def obtener_informacion(self):
            return f"ID: {self.id_animal}, Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Peso: {self.peso} kg."
        def actualizar_peso(self, nuevo_peso):
            self.peso = nuevo_peso
            return f"El peso de {self.nombre} ha sido actualizado a {self.peso} kg."
        def envejecer(self, años):
            self.edad += años
            return f"{self.nombre} ahora tiene {self.edad} años."
        def jugar(self, duracion):
            return f"{self.nombre} ha jugado por {duracion} minutos."
        def revision_medica(self, detalle_revision):
            return f"Revision medica de {self.nombre}: {detalle_revision}."
        def cambiar
        