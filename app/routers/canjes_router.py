from fastapi import APIRouter, status
from app.models.canjes import CanjeSchema
from app.services.canjes_service import registrar_canje_seguro, obtener_vista_historial

router = APIRouter(
    prefix="/canjes",
    tags=["Módulo de Canjes"]
)


@router.post("/crear", status_code=status.HTTP_201_CREATED)
async def realizar_canje(payload: CanjeSchema):
    return await registrar_canje_seguro(
        rut_vecino=payload.rut_vecino,
        nombre_beneficio=payload.nombre_beneficio,
        descripcion=payload.descripcion
    )


@router.get("/historial-vista", status_code=status.HTTP_200_OK)
async def ver_historial_canjes():
    return await obtener_vista_historial()