from pydantic import BaseModel


class CreateTarjetaRequest(BaseModel):
    
    rut: str 
    