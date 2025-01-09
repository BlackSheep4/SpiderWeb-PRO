import re
from pydantic import BaseModel, EmailStr, validator

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str

    @validator("hashed_password")
    # cls = Clase a la que hace referencia, en este caso UserCreate
    # value = Valor que valida, en este caso hashed_password
    def validate_password(cls, value):
        # Regex para validar la contraseña
        password_regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        
        if not re.match(password_regex, value):
            raise ValueError("Password must have at least 8 characters, one uppercase, one number and one special character")
        return value

class UserRead(BaseModel):
    id: int
    name: str
    email: str

    # Esta clase permite que los modelos pydantic funcionen con ORMs (Object-Relational Mappers)
    # Esto facilita la conversión de objetos de la base de datos en datos JSON
    class Config:
        orm_mode = True