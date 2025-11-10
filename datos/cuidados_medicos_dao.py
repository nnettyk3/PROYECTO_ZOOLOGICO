
# datos/cuidados_medicos_dao.py (SQLite)

from modelos.cuidados_medicos import CuidadoMedico
from datos.db_connector import DBConnector
import sqlite3

class CuidadoMedicoDAO:
    def __init__(self):
        self.connector = DBConnector()

    def insertar(self, cuidado):
        """[CREATE] Registra un nuevo cuidado médico."""
        conn = self.connector.connect()
        if not conn: return False, "Error de conexión."
        
        cursor = conn.cursor()
        query = """INSERT INTO cuidados_medicos (id_animal, fecha, tipo_cuidado, descripcion, veterinario, observaciones) 
                 VALUES (?, ?, ?, ?, ?, ?);"""
        
        fecha_str = cuidado.fecha.strftime('%Y-%m-%d')
        valores = (cuidado.id_animal, fecha_str, cuidado.tipo_cuidado, 
                   cuidado.descripcion, cuidado.veterinario, cuidado.observaciones)
        
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