from fastapi import APIRouter

from app.models.auth_model import CreateUsuarioRequest
from app.services.auth_service import create_usuario

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/registro")
def registrar_usuario(data: CreateUsuarioRequest):

    return create_usuario(data)