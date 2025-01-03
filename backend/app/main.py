from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.database import get_db
from backend.app.db.models.user import User as UserModel
from backend.app.schemas.user import UserCreate

app = FastAPI()

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a user in the database
    Verify if user exists. In that case Exception is raised
    """
    # Verificar si el email ya está registrado
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Crear un nuevo usuario
    new_user = UserModel(name=user.name, email=user.email, hashed_password=user.hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@app.get("/users/", response_model=list[UserCreate])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get all users from the database
    """
    users = db.query(UserModel).offset(skip).limit(limit).all()
    return users