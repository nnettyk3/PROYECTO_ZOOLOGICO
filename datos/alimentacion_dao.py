
# datos/alimentacion_dao.py (SQLite)

from modelos.alimentacion import Alimentacion
from datos.db_connector import DBConnector
import sqlite3

class AlimentacionDAO:
    def __init__(self):
        self.connector = DBConnector()

    def insertar(self, alimentacion):
        """[CREATE] Registra la alimentación."""
        conn = self.connector.connect()
        if not conn: return False, "Error de conexión."
        
        cursor = conn.cursor()
        query = """INSERT INTO alimentacion (id_animal, tipo_comida, cantidad, horario) 
                 VALUES (?, ?, ?, ?);"""
        
        # Formato de fecha y hora para SQLite
        horario_str = alimentacion.horario.strftime('%Y-%m-%d %H:%M:%S')
        valores = (alimentacion.id_animal, alimentacion.tipo_comida, 
                   alimentacion.cantidad, horario_str)
        
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