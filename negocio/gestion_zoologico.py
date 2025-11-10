
# Módulo: negocio/gestion_zoologico.py

from datos.cuidador_dao import CuidadorDAO 
from datos.animal_dao import AnimalDAO
from modelos.animal import Animal
from auxiliares.validaciones import validar_texto_no_vacio, validar_entero_positivo 

class GestionZoologico:
    """Contiene la lógica principal y las reglas de negocio del zoológico."""
    
    def __init__(self):
        self.cuidador_dao = CuidadorDAO()
        self.animal_dao = AnimalDAO()

    # --- Operaciones READ ---
    def obtener_lista_cuidadores(self):
        return self.cuidador_dao.obtener_todos()

    def obtener_lista_animales(self):
        return self.animal_dao.obtener_todos()

    # --- Operaciones CREATE ---
    def registrar_nuevo_animal(self, nombre, especie, edad, habitat):
        """Aplica reglas de negocio y registra un animal."""
        
        # 1. Validación de Reglas de Negocio
        if not validar_texto_no_vacio(nombre):
            return False, "El nombre del animal es obligatorio."
        if not validar_texto_no_vacio(especie):
            return False, "La especie es obligatoria."
        if not validar_entero_positivo(edad):
            return False, "La edad debe ser un número entero válido (o cero)."
        
        # 2. Creación del Objeto Modelo
        nuevo_animal = Animal(
            id_animal=None, 
            nombre=nombre, 
            especie=especie, 
            edad=int(edad) if edad else 0, # Convierte a int si no es None
            habitat=habitat
        )

        # 3. Delegación al DAO
        exito, resultado = self.animal_dao.insertar(nuevo_animal)
        
        if exito:
            return True, f"Animal '{nombre}' registrado con ID: {resultado}."
        else:
            return False, f"Fallo al registrar: {resultado}"
            
    # Aquí irán los métodos: asignar_cuidador_a_animal, vender_entrada, etc.