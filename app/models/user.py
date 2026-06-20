from pydantic import BaseModel, EmailStr
from datetime import date

#el modelo que pasaremos por json de persona
class User(BaseModel):
    
    rut: str
    serial_number: str
    
    nombres: str
    apellidos: str
    
    direccion: str | None = None
    numero_direccion: str | None = None
    telefono: str | None = None
    email: EmailStr | None = None
    fecha_nacimiento: date | None = None
    