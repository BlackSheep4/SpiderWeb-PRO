from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.database import get_db
from backend.app.db.models.user import User as UserModel
from backend.app.schemas.user import UserCreate, UserRead
from backend.app.utils.security import hash_password

app = FastAPI()

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a user in the database
    Verify if user exists. In that case Exception is raised
    """
    # Verificar si el email ya está registrado
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hashear la contraseña antes de guardarla
    hashed_password = hash_password(user.hashed_password)
    # Crear un nuevo usuario con la contraseña ya hasheada
    new_user = UserModel(name=user.name, email=user.email, hashed_password=hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@app.get("/users/", response_model=list[UserRead])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get all users from the database
    """
    users = db.query(UserModel).offset(skip).limit(limit).all()
    return users

@app.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user from the database
    """
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Ruta para Actualizar un Usuario
@app.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    """
    Update a user in the database
    """
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Verificar si el nuevo email ya está en uso por otro usuario
    existing_user = db.query(UserModel).filter(UserModel.email == user.email, UserModel.id != user.id).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user from the database
    """
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}