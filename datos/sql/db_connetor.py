
# Módulo: datos/db_connector.py

import sqlite3
from sqlite3 import Error

# Nombre del archivo donde se guardarán los datos
DB_FILE = 'zoologico.db'

class DBConnector:
    """Clase para manejar la conexión y operaciones generales de SQLite."""
    
    def __init__(self):
        self.connection = None

    def connect(self):
        """Establece la conexión a la base de datos SQLite."""
        try:
            # Crea el archivo de base de datos si no existe
            self.connection = sqlite3.connect(DB_FILE)
            self.inicializar_tablas() 
            return self.connection
        except Error as e:
            print(f"Error de conexión a SQLite: {e}")
            return None

    def close(self):
        """Cierra la conexión si está abierta."""
        if self.connection:
            self.connection.close()

    def inicializar_tablas(self):
        """
        Crea todas las tablas necesarias si no existen. 
        Nota: SQLite tiene tipos de datos más simples que MySQL.
        """
        if not self.connection:
            return

        cursor = self.connection.cursor()
        
        # --- DDL (SQL para SQLite) ---
        # Asegúrate de que este DDL coincida con la estructura de tus modelos.

        DDL_SQL = """
        -- Tablas principales
        CREATE TABLE IF NOT EXISTS animal (
            id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especie TEXT NOT NULL,
            edad INTEGER,
            habitat TEXT
        );

        CREATE TABLE IF NOT EXISTS cuidadores (
            id_cuidador INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            turno TEXT,
            especialidad TEXT
        );

        CREATE TABLE IF NOT EXISTS visitantes (
            id_visitante INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            rut TEXT UNIQUE
        );

        -- Tablas de datos/relación
        CREATE TABLE IF NOT EXISTS cuidador_animal (
            id_cuidador INTEGER NOT NULL,
            id_animal INTEGER NOT NULL,
            PRIMARY KEY (id_cuidador, id_animal),
            FOREIGN KEY (id_cuidador) REFERENCES cuidadores(id_cuidador),
            FOREIGN KEY (id_animal) REFERENCES animal(id_animal)
        );

        CREATE TABLE IF NOT EXISTS cuidados_medicos (
            id_cuidado_medico INTEGER PRIMARY KEY AUTOINCREMENT,
            id_animal INTEGER NOT NULL,
            fecha DATE NOT NULL,
            tipo_cuidado TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            veterinario TEXT NOT NULL,
            observaciones TEXT,
            FOREIGN KEY (id_animal) REFERENCES animal(id_animal)
        );

        CREATE TABLE IF NOT EXISTS entrada (
            id_entrada INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_visita DATE NOT NULL,
            precio REAL NOT NULL,
            id_visitante INTEGER,
            FOREIGN KEY (id_visitante) REFERENCES visitantes(id_visitante)
        );

        CREATE TABLE IF NOT EXISTS alimentacion (
            id_alimentacion INTEGER PRIMARY KEY AUTOINCREMENT,
            id_animal INTEGER NOT NULL,
            tipo_comida TEXT NOT NULL,
            cantidad TEXT,
            horario DATETIME,
            FOREIGN KEY (id_animal) REFERENCES animal(id_animal)  
        );
        """
        try:
            cursor.executescript(DDL_SQL) # executescript permite múltiples comandos
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error al inicializar tablas: {e}")
            return False
        finally:
            cursor.close()