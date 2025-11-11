from prettytable import PrettyTable
from datos.insertar_datos import insertar_objeto
from modelos.animal import Animal

def registrar_animal():
    print("\n--- Registro de Nuevo Animal ---")
    nombre = input("Nombre del Animal: ")
    especie = input("Especie: ")
    edad = input("Edad (años): ") 
    habitat = input("Hábitat: ")
        
    nuevo_aninmal = Animal(nombre=nombre, especie=especie, edad=int(edad), habitat=habitat)
    insertar_objeto(nuevo_aninmal)

def mostrar_animales(self):
    animales = self.gestion.obtener_lista_animales()
    if not animales:
        print("No hay animales registrados.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Especie", "Edad", "Hábitat"]
    for a in animales:
        tabla.add_row([a.id_animal, a.nombre, a.especie, a.edad, a.habitat])
    print("\n--- Listado de Animales ---")
    print(tabla)

def asociar_cuidador_a_animal(self):
        print("\n--- Asignación de Cuidador ---")
        # Es recomendable mostrar listas de IDs de Animales y Cuidadores aquí
        id_cuidador = input("Ingrese el ID del Cuidador a asignar: ")
        id_animal = input("Ingrese el ID del Animal: ")
        
        exito, mensaje = self.gestion.asociar_cuidador_animal(id_cuidador, id_animal)
        self._mostrar_resultado(exito, mensaje)