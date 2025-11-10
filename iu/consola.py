
# Módulo: iu/consola.py

from negocio.gestion_zoologico import GestionZoologico
from prettytable import PrettyTable

class InterfazConsola:
    """Proporciona la interfaz de usuario por comandos de consola."""
    
    def __init__(self):
        self.gestion = GestionZoologico()

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

    def _mostrar_resultado(self, exito, mensaje):
        """Función auxiliar para mostrar el resultado de una operación."""
        print("\n" + "="*50)
        print(f"RESULTADO: {'ÉXITO' if exito else 'ERROR'}")
        print(mensaje)
        print("="*50)
    
    # =================================================================
    # --- 1. REGISTRO DE ANIMALES ---
    # =================================================================
    def registrar_animal(self):
        print("\n--- Registro de Nuevo Animal ---")
        nombre = input("Nombre del Animal: ")
        especie = input("Especie: ")
        edad = input("Edad (años): ") 
        habitat = input("Hábitat: ")
        
        exito, mensaje = self.gestion.registrar_nuevo_animal(nombre, especie, edad, habitat)
        self._mostrar_resultado(exito, mensaje)

    # =================================================================
    # --- 2. REGISTRO DE CUIDADORES ---
    # =================================================================
    def registrar_cuidador(self):
        print("\n--- Registro de Nuevo Cuidador ---")
        nombre = input("Nombre del Cuidador: ")
        turno = input("Turno (Mañana/Tarde): ") 
        especialidad = input("Especialidad: ")
        
        exito, mensaje = self.gestion.registrar_nuevo_cuidador(nombre, turno, especialidad)
        self._mostrar_resultado(exito, mensaje)

    # =================================================================
    # --- 3. REGISTRO DE VISITANTES ---
    # =================================================================
    def registrar_visitante(self):
        print("\n--- Registro de Nuevo Visitante ---")
        nombre = input("Nombre: ")
        rut = input("RUT (Ej: 12345678-9): ")
        
        exito, mensaje = self.gestion.registrar_visitante(nombre, rut)
        self._mostrar_resultado(exito, mensaje)

    # =================================================================
    # --- 4. REGISTRO DE ALIMENTACIÓN ---
    # =================================================================
    def registrar_alimentacion(self):
        print("\n--- Registro de Alimentación ---")
        id_animal = input("ID del Animal a alimentar: ")
        tipo_comida = input("Tipo de comida: ")
        cantidad = input("Cantidad (Ej: 3.5 kg): ")
        horario = input("Horario (AAAA-MM-DD HH:MM:SS): ")
        
        exito, mensaje = self.gestion.registrar_alimentacion(id_animal, tipo_comida, cantidad, horario)
        self._mostrar_resultado(exito, mensaje)
        
    # =================================================================
    # --- 5. REGISTRO DE CUIDADOS MÉDICOS ---
    # =================================================================
    def registrar_cuidado_medico(self):
        print("\n--- Registro de Cuidado Médico ---")
        id_animal = input("ID del Animal: ")
        fecha_visita = input("Fecha de Visita (AAAA-MM-DD): ")
        tipo_cuidado = input("Tipo de Cuidado (Ej: Vacuna, Cirugía): ")
        descripcion = input("Descripción/Diagnóstico: ")
        veterinario = input("Veterinario: ")
        observaciones = input("Observaciones (opcional): ")

        exito, mensaje = self.gestion.registrar_cuidado_medico(
            id_animal, fecha_visita, tipo_cuidado, descripcion, veterinario, observaciones
        )
        self._mostrar_resultado(exito, mensaje)

    # =================================================================
    # --- 6. ASOCIACIÓN CUIDADOR-ANIMAL ---
    # =================================================================
    def asociar_cuidador_a_animal(self):
        print("\n--- Asignación de Cuidador ---")
        # Es recomendable mostrar listas de IDs de Animales y Cuidadores aquí
        id_cuidador = input("Ingrese el ID del Cuidador a asignar: ")
        id_animal = input("Ingrese el ID del Animal: ")
        
        exito, mensaje = self.gestion.asociar_cuidador_animal(id_cuidador, id_animal)
        self._mostrar_resultado(exito, mensaje)

    # =================================================================
    # --- 7. VENTA DE ENTRADAS ---
    # =================================================================
    def vender_entrada(self):
        print("\n--- Venta de Entradas ---")
        print(f"Tipos disponibles: {list(self.gestion.precios_entradas.keys())}")
        tipo = input("Ingrese el TIPO de entrada: ")
        fecha_visita = input("Fecha de Visita (AAAA-MM-DD): ")
        id_visitante = input("ID del Visitante (Opcional, dejar vacío si no registrado): ")
        
        # Maneja ID de visitante opcional
        id_visitante = int(id_visitante) if id_visitante.isdigit() else None
        
        exito, mensaje = self.gestion.vender_entrada(tipo, fecha_visita, id_visitante)
        self._mostrar_resultado(exito, mensaje)

    # =================================================================
    # --- LECTURA (READ) ---
    # =================================================================
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
        
    def mostrar_visitantes(self):
        # NOTA: Debes implementar obtener_todos en visitante_dao.py
        visitantes = self.gestion.obtener_lista_visitantes()
        if not visitantes:
            print("No hay visitantes registrados.")
            return

        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "RUT"]
        for v in visitantes:
            tabla.add_row([v.id_visitante, v.nombre, v.rut])
        print("\n--- Listado de Visitantes ---")
        print(tabla)

    # =================================================================
    # --- CICLO PRINCIPAL ---
    # =================================================================
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