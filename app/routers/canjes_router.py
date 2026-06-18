from fastapi import APIRouter
from app.services.canjes_service import canjear_beneficio

router = APIRouter(
    prefix="/beneficios",
    tags=["Beneficios"]
)


@router.post("/canjear")
def canjear(
    id_persona: int,
    id_beneficio: int
):
    return canjear_beneficio(
        id_persona,
        id_beneficio
    )
