from prettytable import PrettyTable
from datos.insertar_datos import insertar_objeto
from modelos.animal import Animal
from datos.obtener_datos import obtener_datos_objetos

def registrar_animal():
    print("\n--- Registro de Nuevo Animal ---")
    nombre = input("Nombre del Animal: ")
    especie = input("Especie: ")
    edad = input("Edad (años): ") 
    habitat = input("Hábitat: ")
        
    nuevo_aninmal = Animal(nombre=nombre.title(), especie=especie.title(), edad=int(edad), habitat=habitat.title())
    insertar_objeto(nuevo_aninmal)

def mostrar_animales():
    tabla_animales = PrettyTable()
    tabla_animales.field_names = ['id_animal', 'nombre', 'especie', 'edad', 'habitat']
    listado_animales = obtener_datos_objetos(Animal)
    if listado_animales:
        for animal in listado_animales:
            tabla_animales.add_row(
                [animal.id_animal, animal.nombre, animal.especie, animal. edad, animal.habitat])
        print(tabla_animales)

def asociar_cuidador_a_animal(self):
        print("\n--- Asignación de Cuidador ---")
        # Es recomendable mostrar listas de IDs de Animales y Cuidadores aquí
        id_cuidador = input("Ingrese el ID del Cuidador a asignar: ")
        id_animal = input("Ingrese el ID del Animal: ")
        
        exito, mensaje = self.gestion.asociar_cuidador_animal(id_cuidador, id_animal)
        self._mostrar_resultado(exito, mensaje)