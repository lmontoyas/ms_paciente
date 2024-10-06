from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import time

# Actualiza la URL de conexión
DATABASE_URL = "mysql+pymysql://user:user_password@db/ms_pacientes"

# Crea el motor y la sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
meta_data = MetaData()

# Método para obtener una sesión de base de datos
def get_db():
    retries = 5
    while retries:
        db = SessionLocal()
        try:
            db.execute(text("SELECT 1"))  # Solo una consulta simple para comprobar la conexión
            yield db
            break
        except OperationalError:
            retries -= 1
            time.sleep(5)  # Esperar 5 segundos antes de volver a intentar
    else:
        raise Exception("No se pudo conectar a la base de datos después de varios intentos.")

