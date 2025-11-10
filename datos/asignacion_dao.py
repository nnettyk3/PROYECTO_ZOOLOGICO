
# datos/asignacion_dao.py (SQLite)

from datos.db_connector import DBConnector
import sqlite3

class AsignacionDAO:
    def __init__(self):
        self.connector = DBConnector()

    def asignar_cuidador_a_animal(self, id_cuidador, id_animal):
        """Asigna un cuidador a un animal en la tabla de relación cuidador_animal."""
        conn = self.connector.connect()
        if not conn: return False, "Error de conexión."
        
        cursor = conn.cursor()
        query = "INSERT INTO cuidador_animal (id_cuidador, id_animal) VALUES (?, ?);"
        valores = (id_cuidador, id_animal)
        
        try:
            cursor.execute(query, valores)
            conn.commit()
            return True, "Asignación exitosa."
        except sqlite3.IntegrityError as err:
            conn.rollback()
            # El error 19 (IntegrityError) en SQLite maneja FK no existentes y duplicados
            return False, "Error de integridad: El cuidador/animal no existe o la asignación ya está hecha."
        except sqlite3.Error as err:
            conn.rollback()
            return False, str(err)
        finally:
            cursor.close()
            self.connector.close()