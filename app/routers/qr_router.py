from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.qr_model import QRRequest
from app.services.qr_service import (get_persona_by_rut, generar_qr)

router = APIRouter(
    prefix="/qr",
    tags=["QR"]
)

@router.post("/generar")
def generar_codigo_qr(data: QRRequest):
    
    persona = get_persona_by_rut(data.rut)
    
    imagen = generar_qr(persona)
    
    return StreamingResponse(
        imagen,
        media_type="image/png"
    )