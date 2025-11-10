
# Módulo: negocio/gestion_zoologico.py

# --- Importaciones de Capa de Datos (DAOs) ---
from datos.animal_dao import AnimalDAO
from datos.cuidador_dao import CuidadorDAO
from datos.visitante_dao import VisitanteDAO
from datos.entrada_dao import EntradaDAO
from datos.cuidados_medicos_dao import CuidadoMedicoDAO
from datos.alimentacion_dao import AlimentacionDAO
from datos.asignacion_dao import AsignacionDAO # Asumo que esta clase maneja la tabla cuidador_animal

# --- Importaciones de Modelos ---
from modelos.animal import Animal
from modelos.cuidador import Cuidador
from modelos.visitante import Visitante
from modelos.entrada import Entrada
from modelos.cuidados_medicos import CuidadoMedico
from modelos.alimentacion import Alimentacion

# --- Importaciones de Auxiliares ---
from auxiliares.validaciones import validar_texto_no_vacio, validar_entero_positivo, validar_fecha
from datetime import datetime

class GestionZoologico:
    """Contiene la lógica principal del sistema, aplica reglas de negocio y coordina los DAOs."""
    
    def __init__(self):
        # Inicialización de todos los DAOs
        self.animal_dao = AnimalDAO()
        self.cuidador_dao = CuidadorDAO()
        self.visitante_dao = VisitanteDAO()
        self.entrada_dao = EntradaDAO()
        self.cuidados_medicos_dao = CuidadoMedicoDAO()
        self.alimentacion_dao = AlimentacionDAO()
        self.asignacion_dao = AsignacionDAO()
        
        # Regla de Negocio: Precios de entradas (ejemplo)
        self.precios_entradas = {
            'ADULTO': 7000.00,
            'NIÑO': 5000.00,
            'FAMILIAR': 20000.00
        }

    # =================================================================
    # --- 1. Lógica de ANIMALES (CREATE) ---
    # =================================================================

    def registrar_nuevo_animal(self, nombre, especie, edad, habitat):
        """Aplica reglas y registra un animal."""
        if not validar_texto_no_vacio(nombre) or not validar_texto_no_vacio(especie):
            return False, "Nombre y especie son obligatorios."
        if not validar_entero_positivo(edad):
            return False, "La edad debe ser un número entero válido."

        nuevo_animal = Animal(id_animal=None, nombre=nombre, especie=especie, edad=int(edad), habitat=habitat)
        return self.animal_dao.insertar(nuevo_animal)

    # =================================================================
    # --- 2. Lógica de CUIDADORES (CREATE) ---
    # =================================================================

    def registrar_nuevo_cuidador(self, nombre, turno, especialidad):
        """Aplica reglas y registra un cuidador."""
        if not validar_texto_no_vacio(nombre):
            return False, "El nombre del cuidador es obligatorio."
        # Se pueden añadir reglas sobre turnos o especialidades si es necesario.

        nuevo_cuidador = Cuidador(id_cuidador=None, nombre=nombre, turno=turno, especialidad=especialidad)
        return self.cuidador_dao.insertar(nuevo_cuidador)
        
    # =================================================================
    # --- 3. Lógica de ASOCIACIÓN (CREATE en tabla relacional) ---
    # =================================================================

    def asociar_cuidador_animal(self, id_cuidador, id_animal):
        """Asocia un cuidador a un animal mediante sus IDs."""
        if not validar_entero_positivo(id_cuidador) or not validar_entero_positivo(id_animal):
            return False, "Ambos IDs deben ser números enteros positivos."
        
        # Regla de Negocio implícita: Delegamos al DAO para que valide FK (existencia)
        return self.asignacion_dao.asignar_cuidador_a_animal(int(id_cuidador), int(id_animal))

    # =================================================================
    # --- 4. Lógica de ENTRADAS y VISITANTES (CREATE) ---
    # =================================================================
    
    def registrar_visitante(self, nombre, rut):
        """Registra un visitante antes de la venta de entradas."""
        if not validar_texto_no_vacio(nombre) or not validar_texto_no_vacio(rut):
            return False, "Nombre y RUT son obligatorios para el registro de visitantes."
        
        # Regla de Negocio: Podrías validar el formato del RUT aquí
        
        nuevo_visitante = Visitante(id_visitante=None, nombre=nombre, rut=rut)
        return self.visitante_dao.insertar(nuevo_visitante)


    def vender_entrada(self, tipo_entrada, fecha_visita_str, id_visitante=None):
        """Vende una entrada, calculando el precio y registrando la fecha."""
        
        # 1. Validación de Reglas de Negocio
        tipo_entrada = tipo_entrada.strip().upper()
        if tipo_entrada not in self.precios_entradas:
            return False, f"Tipo de entrada no válido. Opciones: {list(self.precios_entradas.keys())}"
        
        fecha_obj = validar_fecha(fecha_visita_str)
        if not fecha_obj:
            return False, "Formato de fecha de visita inválido. Use AAAA-MM-DD."

        precio = self.precios_entradas[tipo_entrada]
        
        # 2. Creación del Objeto Entrada
        nueva_entrada = Entrada(
            id_entrada=None,
            fecha_visita=fecha_obj, # El DAO se encargará de formatear a string si es necesario
            precio=precio,
            id_visitante=id_visitante # Puede ser None
        )
        
        # 3. Delegación al DAO
        exito, resultado = self.entrada_dao.insertar(nueva_entrada)

        if exito:
            return True, f"Venta {tipo_entrada} exitosa (ID {resultado}) por ${precio:.2f}."
        else:
            return False, f"Fallo en la venta: {resultado}"

    # =================================================================
    # --- 5. Lógica de EXTENSIONES (Cuidados y Alimentación - CREATE) ---
    # =================================================================

    def registrar_cuidado_medico(self, id_animal, fecha_visita_str, tipo, desc, vet, obs):
        """Registra un cuidado médico asociado a un animal."""
        if not validar_entero_positivo(id_animal):
            return False, "ID de animal inválido."
            
        fecha_obj = validar_fecha(fecha_visita_str)
        if not fecha_obj:
            return False, "Formato de fecha inválido. Use AAAA-MM-DD."
            
        # Podrías validar que el animal exista, pero el FK en el DAO lo hará.
        
        nuevo_cuidado = CuidadoMedico(
            id_cuidado_medico=None, id_animal=int(id_animal), fecha_visita=fecha_obj, 
            tipo_cuidado=tipo, descripcion=desc, veterinario=vet, observaciones=obs
        )
        return self.cuidados_medicos_dao.insertar(nuevo_cuidado)

    def registrar_alimentacion(self, id_animal, tipo_comida, cantidad, horario_str):
        """Registra la alimentación de un animal."""
        if not validar_entero_positivo(id_animal):
            return False, "ID de animal inválido."
            
        try:
            horario_obj = datetime.strptime(horario_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return False, "El formato de horario debe ser AAAA-MM-DD HH:MM:SS."
        
        nueva_alimentacion = Alimentacion(
            id_alimentacion=None, id_animal=int(id_animal), tipo_comida=tipo_comida, 
            cantidad=cantidad, horario=horario_obj
        )
        return self.alimentacion_dao.insertar(nueva_alimentacion)
        
    # =================================================================
    # --- Operaciones de Lectura (READ) ---
    # =================================================================

    def obtener_lista_cuidadores(self):
        return self.cuidador_dao.obtener_todos()

    def obtener_lista_animales(self):
        return self.animal_dao.obtener_todos()
        
    def obtener_lista_visitantes(self):
        return self.visitante_dao.obtener_todos()
        
    # ... (Añadir métodos READ para el resto de entidades)