from negocio.negocio_animal import registrar_animal, mostrar_animales, asociar_cuidador_a_animal
from negocio.negocio_cuidadores import registrar_cuidador, mostrar_cuidadores
from negocio.negocio_visitantes import registrar_visitante, mostrar_visitantes
from negocio.negocio_alimentacion import registrar_alimentacion
from negocio.negocio_cuidados_medicos import registrar_cuidado_medico
from negocio.negocio_entrada import vender_entrada


def menu_principal():
    ejecutando = True
    while ejecutando:   
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
        
        opcion = input("sellecione una opcion:")
            
        if opcion == '1':
            registrar_animal()
        elif opcion == '2':
            registrar_cuidador()
        elif opcion == '3':
            registrar_visitante()
        elif opcion == '4':
            registrar_alimentacion()
        elif opcion == '5':
            registrar_cuidado_medico()
        elif opcion == '6':
            asociar_cuidador_a_animal()
        elif opcion == '7':
            vender_entrada()
        elif opcion == '8':
            mostrar_animales()
        elif opcion == '9':
            mostrar_cuidadores()
        elif opcion == '10':
            mostrar_visitantes()
        elif opcion == '11':
            print("Saliendo del sistema. Adiós!")
            ejecutando = False
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
