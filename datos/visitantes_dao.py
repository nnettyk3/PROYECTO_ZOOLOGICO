
# datos/visitante_dao.py (SQLite)

from modelos.visitante import Visitante
from datos.db_connector import DBConnector
import sqlite3

class VisitanteDAO:
    def __init__(self):
        self.connector = DBConnector()

    def obtener_todos(self):
        """[READ] Obtiene todos los visitantes."""
        conn = self.connector.connect()
        if not conn: return []
        
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = "SELECT id_visitante, nombre, rut FROM visitantes;"
        visitantes = []
        try:
            cursor.execute(query)
            for fila in cursor.fetchall():
                visitantes.append(Visitante(
                    id_visitante=fila['id_visitante'], 
                    nombre=fila['nombre'], 
                    rut=fila['rut']
                ))
        finally:
            cursor.close()
            self.connector.close()
        return visitantes

    def insertar(self, visitante):
        """[CREATE] Inserta un nuevo visitante."""
        conn = self.connector.connect()
        if not conn: return False, "Error de conexión."
        
        cursor = conn.cursor()
        query = "INSERT INTO visitantes (nombre, rut) VALUES (?, ?);"
        valores = (visitante.nombre, visitante.rut)
        
        try:
            cursor.execute(query, valores)
            conn.commit()
            return True, cursor.lastrowid
        except sqlite3.Error as err:
            conn.rollback()
            # Error de integridad para UNIQUE (rut)
            if "UNIQUE constraint failed" in str(err):
                return False, "El RUT ya se encuentra registrado."
            return False, str(err)
        finally:
            cursor.close()
            self.connector.close()