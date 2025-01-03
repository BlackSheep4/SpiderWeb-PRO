from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    hashed_password: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True