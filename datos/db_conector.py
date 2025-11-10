

import mysql.connector
from modelos.animal import Animal
from modelos.cuidador import Cuidador # Asegúrate de importar el modelo Cuidador

# --- ⚠️ CONFIGURACIÓN CLAVE ⚠️ ---
# ¡DEBES REEMPLAZAR ESTOS VALORES CON TU ENTORNO REAL DE MYSQL!
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root', # Ejemplo
    'password': 'tu_password_aqui', # Ejemplo
    'database': 'proyecto_zoologico_db' # Ejemplo
}

class DBConnector:
    """Clase base para manejar la conexión y operaciones generales de la BBDD."""
    
    def __init__(self):
        self.connection = None

    def connect(self):
        """Establece la conexión a la BBDD."""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            return self.connection
        except mysql.connector.Error as err:
            print(f"Error de conexión a MySQL: {err}")
            return None

    def close(self):
        """Cierra la conexión si está abierta."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            # print("Conexión a BBDD cerrada.") # Puedes descomentar para depuración
# ...