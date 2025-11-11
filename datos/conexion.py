
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# pip install sqlalchemy
# pip install mysql-connector-python

# Definir cadena de conexion
# mysql+mysqlconnector://user:password@host:port/database_name
# Reemplazar user, password, host, port, y database con sus credenciales de DB
url_db = "mysql+mysqlconnector://root:@localhost:3306/PROYECTO_ZOOLOGICO"
motor_db = create_engine(url_db)
Session = sessionmaker(bind=motor_db)
sesion = Session()