
from negocio.zoologico_service import ZoologicoService

def mostrar_menu():
    servicio = ZoologicoService()
    while True:
        print("\n=== MENÚ ZOOLÓGICO ===")
        print("1. Listar animales")
        print("2. Registrar animal")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            animales = servicio.mostrar_animales()
            for a in animales:
                print(a)
        elif opcion == "2":
            nombre = input("Nombre: ")
            especie = input("Especie: ")
            edad = int(input("Edad: "))
            habitat = input("Hábitat: ")
            servicio.registrar_animal(nombre, especie, edad, habitat)
        elif opcion == "3":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")
