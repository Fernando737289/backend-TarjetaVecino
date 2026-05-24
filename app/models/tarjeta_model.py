from pydantic import BaseModel
from datetime import date


class CreateTarjetaRequest(BaseModel):
    
    rut: str 
    nombres: str
    apellidos: str
    telefono: str | None = None
    
class UpdateTarjetaRequest(BaseModel):
    
    estado: str
    fecha_vencimiento: date
