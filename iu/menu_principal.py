
def mostrar_menu(self):
        print("\n=== Sistema de Gestión Zoológico (CRUD) ===")
        print("--- REGISTROS (CREATE) ---")
        print("1. Registrar Animal")
        print("2. Registrar Cuidador")
        print("3. Registrar Visitante")
        print("4. Registrar Alimentación")
        print("5. Registrar Cuidado Médico")
        print("--- OPERACIONES ---")
        print("6. Asociar Cuidador a Animal")
        print("7. Vender Entrada")
        print("--- LECTURA (READ) ---")
        print("8. Mostrar Animales")
        print("9. Mostrar Cuidadores")
        print("10. Mostrar Visitantes")
        print("11. Salir")
        return input("Seleccione una opción: ")

def iniciar(self):
    while True:
        try:
            opcion = input(self.mostrar_menu()).strip()
        except EOFError:
            opcion = '11' # Permite salir en ambientes interactivos
            
        if opcion == '1':
            self.registrar_animal()
        elif opcion == '2':
            self.registrar_cuidador()
        elif opcion == '3':
            self.registrar_visitante()
        elif opcion == '4':
            self.registrar_alimentacion()
        elif opcion == '5':
            self.registrar_cuidado_medico()
        elif opcion == '6':
            self.asociar_cuidador_a_animal()
        elif opcion == '7':
            self.vender_entrada()
        elif opcion == '8':
            self.mostrar_animales()
        elif opcion == '9':
            self.mostrar_cuidadores()
        elif opcion == '10':
            self.mostrar_visitantes()
        elif opcion == '11':
            print("Saliendo del sistema. Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")