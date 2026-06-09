from fastapi import APIRouter

from app.models.beneficio_model import Beneficio
from app.services.beneficio_service import (
    create_beneficio,
    list_beneficios
)

router = APIRouter(
    prefix="/beneficios",
    tags=["Beneficios"]
)

@router.post("/crear")
def crear_beneficio(data: Beneficio):

    return create_beneficio(data)

@router.get("/")
def obtener_beneficios():

    return list_beneficios()