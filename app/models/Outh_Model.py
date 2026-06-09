from pydantic import BaseModel, EmailStr

class CreateUsuarioRequest(BaseModel):

    usuario: str
    correo: EmailStr
    password: str