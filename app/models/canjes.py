from pydantic import BaseModel

class CanjeSchema(BaseModel):
    rut_vecino: str
    nombre_beneficio: str
    descripcion: str