from fastapi import APIRouter

from app.models.tarjeta_model import CreateTarjetaRequest, UpdateTarjetaRequest
from app.services.tarjeta_service import (
    create_tarjeta,
    get_tarjeta,
    update_tarjeta,
    delete_tarjeta
)
from app.services.vigencia_service import validar_vigencia

router = APIRouter(
    prefix="/tarjeta",
    tags=["Tarjeta"]
)


@router.post("/crear")
def crear_tarjeta(data: CreateTarjetaRequest):

    return create_tarjeta(
        data.rut,
        data.nombres,
        data.apellidos,
        data.telefono
    )


@router.get("/rut/{rut}")
def obtener_tarjeta(rut: str):

    return get_tarjeta(rut)


@router.put("/{id_tarjeta}")
def actualizar_tarjeta(id_tarjeta: int, data: UpdateTarjetaRequest):

    return update_tarjeta(
        id_tarjeta,
        data.estado,
        data.fecha_vencimiento
    )


@router.delete("/{id_tarjeta}")
def eliminar_tarjeta(id_tarjeta: int):

    return delete_tarjeta(id_tarjeta)

##prueba con apikey

@router.post("/validar-vigencia")
async def validar(data: dict):

    api_key = "TU_API_KEY"

    resultado = await validar_vigencia(
        data["user_rut"],
        data["serial_number"],
        api_key
    )

    return resultado