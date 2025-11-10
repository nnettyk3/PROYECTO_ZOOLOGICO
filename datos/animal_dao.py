
# Módulo: datos/animal_dao.py (Adaptado para SQLite)

from modelos.animal import Animal
from datos.db_connector import DBConnector 
import sqlite3

class AnimalDAO:
    def __init__(self):
        self.connector = DBConnector()

    def obtener_todos(self):
        """[READ] Mapea filas SQL a objetos Animal."""
        conn = self.connector.connect()
        if not conn: return []
        
        # En SQLite, 'row_factory' nos permite obtener resultados como diccionarios
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        query = "SELECT id_animal, nombre, especie, edad, habitat FROM animal;"
        animales = []
        try:
            cursor.execute(query)
            for fila in cursor.fetchall():
                # sqlite3.Row permite acceder a los datos como fila['nombre']
                animales.append(Animal(
                    id_animal=fila['id_animal'], 
                    nombre=fila['nombre'], 
                    especie=fila['especie'], 
                    edad=fila['edad'], 
                    habitat=fila['habitat']
                ))
        finally:
            cursor.close()
            self.connector.close()
        return animales

    def insertar(self, animal):
        """[CREATE] Inserta un nuevo animal."""
        conn = self.connector.connect()
        if not conn: return False, "Error de conexión."
        
        cursor = conn.cursor()
        query = "INSERT INTO animal (nombre, especie, edad, habitat) VALUES (?, ?, ?, ?);"
        # En SQLite, usamos '?' como placeholder
        valores = (animal.nombre, animal.especie, animal.edad, animal.habitat)
        
        try:
            cursor.execute(query, valores)
            conn.commit() 
            return True, cursor.lastrowid
        except sqlite3.Error as err:
            conn.rollback() 
            return False, str(err)
        finally:
            cursor.close()
            self.connector.close()