from passlib.context import CryptContext

# Algoritmo de hashing utilizado es bcrypt
# Para manejar algortimos de hashing obsoletos se utiliza el parámetro
# deprecated="auto", que permite que las contraseñas funcionen igualmente
# Se usa bcrypt por que añade automáticamente una sal (salt), que es un
# valor aleatorio que hace que los hashes sean únicos incluso si dos personas
# tienen la misma contraseña
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Genera un hash seguro para la contraseña
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica que la contraseña introducida sea correcta
    """
    return pwd_context.verify(plain_password, hashed_password)