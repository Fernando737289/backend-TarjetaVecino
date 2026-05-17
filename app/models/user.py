from pydantic import BaseModel, EmailStr
from datetime import date

class User(BaseModel):
    
    
    rut: str
    nombres: str
    apellidos: str
    direccion: str | None = None
    numero_direccion: str | None = None
    telefono: str | None = None
    email: EmailStr | None = None
    fecha_nacimiento: date | None = None