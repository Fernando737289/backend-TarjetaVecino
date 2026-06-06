from pydantic import BaseModel

class VerificacionCedulaSchema(BaseModel):
    user_rut: str 
    serial_number: str 