from prettytable import PrettyTable

def registrar_animal(self):
    print("\n--- Registro de Nuevo Animal ---")
    nombre = input("Nombre del Animal: ")
    especie = input("Especie: ")
    edad = input("Edad (años): ") 
    habitat = input("Hábitat: ")
        
    exito, mensaje = self.gestion.registrar_nuevo_animal(nombre, especie, edad, habitat)
    self._mostrar_resultado(exito, mensaje)

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