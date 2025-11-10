
# Módulo: iu/consola.py

from negocio.gestion_zoologico import GestionZoologico
from prettytable import PrettyTable

class InterfazConsola:
    """Proporciona la interfaz de usuario por comandos de consola."""
    
    def __init__(self):
        self.gestion = GestionZoologico()

    def mostrar_menu(self):
        print("\n=== Sistema de Gestión Zoológico ===")
        print("1. Registrar Animal (CREATE)")
        print("2. Mostrar Cuidadores (READ)")
        print("3. Mostrar Animales (READ)")
        print("4. Vender Entrada")
        print("5. Salir")
        return input("Seleccione una opción: ")

    # --- CREATE ---
    def registrar_animal(self):
        print("\n--- 🦒 Registro de Nuevo Animal ---")
        nombre = input("Nombre del Animal: ")
        especie = input("Especie: ")
        edad = input("Edad (años, opcional): ") 
        habitat = input("Hábitat: ")
        
        exito, mensaje = self.gestion.registrar_nuevo_animal(nombre, especie, edad, habitat)
        
        print("\n" + "="*50)
        print(f"RESULTADO: {'✅ ÉXITO' if exito else '❌ ERROR'}")
        print(mensaje)
        print("="*50)

    # --- READ ---
    def mostrar_cuidadores(self):
        cuidadores = self.gestion.obtener_lista_cuidadores()
        
        if not cuidadores:
            print("No se encontraron cuidadores.")
            return

        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Turno", "Especialidad"]
        
        for c in cuidadores:
            tabla.add_row([c.id_cuidador, c.nombre, c.turno, c.especialidad])
        
        print("\n--- Listado de Cuidadores ---")
        print(tabla)

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

    def iniciar(self):
        while True:
            opcion = self.mostrar_menu()
            if opcion == '1':
                self.registrar_animal()
            elif opcion == '2':
                self.mostrar_cuidadores()
            elif opcion == '3':
                self.mostrar_animales()
            elif opcion == '5':
                print("Saliendo del sistema. ¡Adiós!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")