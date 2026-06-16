from fastapi import APIRouter
from app.services.canjes_service import canjear_beneficio

router = APIRouter(
    prefix="/beneficios",
    tags=["Beneficios"]
)


@router.post("/canjear")
def canjear(
    rut: str,
    id_beneficio: int
):
    return canjear_beneficio(
        rut,
        id_beneficio
    )