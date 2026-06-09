from fastapi import APIRouter

from app.models.Outh_Model import CreateUsuarioRequest
from app.services.Outh_service import create_usuario

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/registro")
def registrar_usuario(data: CreateUsuarioRequest):

    return create_usuario(data)