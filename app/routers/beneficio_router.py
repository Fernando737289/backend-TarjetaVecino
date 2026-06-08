from fastapi import APIRouter

from app.models.beneficio_model import Beneficio
from app.services.beneficio_service import (
    create_beneficio,
    list_beneficios,
    update_beneficio,
    delete_beneficio
)

router = APIRouter(
    prefix="/beneficios",
    tags=["Beneficios"]
)

@router.post("/crear")
def crear_beneficio(data: Beneficio):

    return create_beneficio(data)

@router.get("/")
def obtener_beneficios():

    return list_beneficios()

@router.put("/actualizar/{id_beneficio}")
def actualizar_beneficio(id_beneficio: int, data: Beneficio):

    return update_beneficio(id_beneficio, data)


@router.delete("/eliminar/{id_beneficio}")
def eliminar_beneficio(id_beneficio: int):

    return delete_beneficio(id_beneficio)