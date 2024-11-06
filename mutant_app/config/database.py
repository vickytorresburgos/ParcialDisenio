import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError
from models.dna import base

# configuracion de variables de entorno

load_dotenv()

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

def check_postgres_service(): # verifica si el servicio de POSTGRESQL esta activo y responde
    temp_engine = create_engine(DATABASE_URI)
    try:
        with temp_engine.connect() as connection:
            connection.execute(text("SELECT 1")) # ejecta una consulta para verificar que el servicio este activo
        return True
    except OperationalError: # manejo de errores
        return False
    finally:
        temp_engine.dispose()

class Database: # maneja conexion y operaciones con la bd 
    _instance = None # implementada como singleton -> solo hay una instancia
    engine = create_engine(DATABASE_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def __init__(self):
        self._session = None # inicializa la sesion

    def __new__(cls):
        if not cls._instance: # si _isinstance no se ha definido crea una instancia y le asigna _isinstance
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._engine = cls.engine
            cls._instance._SessionLocal = cls.SessionLocal
        return cls._instance

    def get_session(self) -> Session: # obtiene una sesion de base de datos
        if self._session is None: # si es none crea una nueva sesion
            self._session = self._SessionLocal()
        return self._session

    def drop_database(self): # elimina todas las tablas de los modelos 
        try:
            base.metadata.drop_all(self._engine)
            print("Tablas eliminadas correctamente.")
        except Exception as e:
            print(f"Error eliminando tablas: {e}")

    def create_tables(self): # crea las tablas de la base de datos
        try:
            base.metadata.create_all(self.engine)
            print("Tablas creadas correctamente.")
        except Exception as e:
            print(f"Error creando tablas: {e}")

    def close_session(self): # cierra la sesion de la base de datos
        if hasattr(self, "_session"):
            self._session.close()
            del self._session

    def check_connection(self): # comprueba si la base de datos es accesible
        try:
            with self._engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Conexión establecida.")
            return True
        except Exception as e:
            print(f"Error de conexión a la base de datos: {e}")
            return False
        

# patron singleton
# uso de variables de entorno
# manejo de sesiones
# manejo de errores
# gestion de tablas
# single responsability principle
