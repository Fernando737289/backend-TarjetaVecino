from fastapi import APIRouter, Depends

from app.models.Outh_Model import CreateUsuarioRequest
from app.services.Outh_service import create_usuario
from app.core.dependencies import require_admin

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/registro")
def registrar_usuario(
    data: CreateUsuarioRequest,
    admin = Depends(require_admin)
):

    return create_usuario(data)