from fastapi import APIRouter
from app.services.canjes_service import canjear_beneficio
from app.services.historial_beneficio_service import obtener_historial_persona

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

@router.get("/historial/{id_persona}")
def historial_persona(id_persona: int):

    return obtener_historial_persona(id_persona)