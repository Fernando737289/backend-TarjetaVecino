from pydantic import BaseModel, EmailStr

class CreateUsuarioRequest(BaseModel):

    username: str
    email: EmailStr
    password: str
    