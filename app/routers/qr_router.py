from fastapi import APIRouter
from app.models.qr_model import QRRequest
from app.services.qr_service import (get_persona_by_rut, generar_qr)

router = APIRouter(
    prefix="/qr",
    tags=["QR"]
)

@router.post("/generar")
def generar_codigo_qr(data: QRRequest):
    
    persona = get_persona_by_rut(data.rut)
    
    base64_qr = generar_qr(persona)
    
    return {
         "longitud": len(base64_qr)
    }
       
