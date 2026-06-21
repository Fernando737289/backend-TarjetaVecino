ffrom fastapi import APIRouter, Depends

from app.services.auditoria_service import list_auditoria
from app.core.dependencies import require_admin

router = APIRouter(
    prefix="/auditoria",
    tags=["Auditoria"]
)


@router.get("/")
def obtener_auditoria(
    admin=Depends(require_admin)
):

    return list_auditoria()
