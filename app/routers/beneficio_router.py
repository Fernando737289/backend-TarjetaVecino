from fastapi import APIRouter, Depends

from app.models.beneficio_model import Beneficio
from app.services.beneficio_service import (
    create_beneficio,
    list_beneficios,
    update_beneficio,
    delete_beneficio
)
from app.core.dependencies import require_admin
from app.core.auditoria import registrar_auditoria

router = APIRouter(
    prefix="/beneficios",
    tags=["Beneficios"]
)

@router.post("/crear")
def crear_beneficio(
    data: Beneficio,
    admin = Depends(require_admin)
):

    resultado = create_beneficio(data)

    registrar_auditoria(
        "beneficios",
        "CREATE",
        f"Se creo el beneficio {data.nombre}",
        admin["sub"]
    )

    return resultado

@router.get("/")
def obtener_beneficios():

    return list_beneficios()

@router.put("/actualizar/{id_beneficio}")
def actualizar_beneficio(
    id_beneficio: int,
    data: Beneficio,
    admin = Depends(require_admin)
):

    resultado = update_beneficio(id_beneficio, data)

    registrar_auditoria(
        "beneficios",
        "UPDATE",
        f"Se actualizo el beneficio {id_beneficio}",
        admin["sub"]
    )

    return resultado


@router.delete("/eliminar/{id_beneficio}")
def eliminar_beneficio(
    id_beneficio: int,
    admin = Depends(require_admin)
):

    resultado = delete_beneficio(id_beneficio)

    registrar_auditoria(
        "beneficios",
        "DELETE",
        f"Se elimino el beneficio {id_beneficio}",
        admin["sub"]
    )

    return resultado