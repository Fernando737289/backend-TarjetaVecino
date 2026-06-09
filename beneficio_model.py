from pydantic import BaseModel
from datetime import date

class Beneficio(BaseModel):

    nombre: str
    descripcion: str | None = None
    tipo_descuento: str
    valor_descuento: float
    stock: int
    fecha_inicio: date
    fecha_vencimiento: date
    comercio: str | None = None