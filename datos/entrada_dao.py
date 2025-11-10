
# datos/entrada_dao.py (SQLite)

from modelos.entrada import Entrada
from datos.db_connector import DBConnector
import sqlite3

class EntradaDAO:
    def __init__(self):
        self.connector = DBConnector()

    def insertar(self, entrada):
        """[CREATE] Registra una nueva entrada."""
        conn = self.connector.connect()
        if not conn: return False, "Error de conexión."
        
        cursor = conn.cursor()
        query = "INSERT INTO entrada (fecha_visita, precio, id_visitante) VALUES (?, ?, ?);"
        
        # En SQLite, las fechas/datetimes se almacenan como texto (ISO8601 string)
        fecha_str = entrada.fecha_visita.strftime('%Y-%m-%d')
        id_vis = entrada.id_visitante if entrada.id_visitante else None 
        valores = (fecha_str, entrada.precio, id_vis)
        
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