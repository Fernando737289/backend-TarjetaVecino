from pydantic import BaseModel

class QRRequest(BaseModel):
    
    rut: str
    