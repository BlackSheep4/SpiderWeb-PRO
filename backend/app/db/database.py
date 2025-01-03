from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear la base de datos SQLite
SQLITE_URL = "sqlite:///./spiderweb.db"

# Motor de conexión
engine = create_engine(SQLITE_URL, connect_args={"check_same_thread": False})

# Sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para las rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
