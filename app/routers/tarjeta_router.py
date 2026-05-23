from fastapi import APIRouter

from app.models.tarjeta_model import CreateTarjetaRequest
from app.services.tarjeta_service import create_tarjeta, get_tarjeta

router = APIRouter(
    prefix="/tarjeta",
    tags=["Tarjeta"]
)


@router.post("/crear")
def crear_tarjeta(data: CreateTarjetaRequest):

    return create_tarjeta(data.rut)

@router.get("/{id_tarjeta}")
def obtener_tarjeta(id_tarjeta: int):
    
    return get_tarjeta(id_tarjeta)