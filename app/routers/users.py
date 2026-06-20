from fastapi import APIRouter, Depends
from app.models.user import (
    User,
    UpdateEstadoPersonaRequest
)
from app.services.user_service import (
    create_user,
    list_users,
    update_user,
    delete_user,
    update_estado_persona
)
from app.core.dependencies import require_admin

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

#rListar personas (publico)
@router.get("/")
def list_all_users():
    return list_users()

# Crear persona (Solo admin) 
@router.post("/usuarios")
async def registrar_usuario(
    payload: User,
    admin = Depends(require_admin)
):
    return await create_user(payload)

# actualizar persona (Solo admin) 
@router.put("/{id_persona}")
def update_users(
    id_persona: int, 
    user: User,
    admin = Depends(require_admin)
):
    return update_user(id_persona, user)


# eliminar persona (Solo admin) 
@router.delete("/{id_persona}")
def delete_users(
    id_persona: int,
    admin = Depends(require_admin)
):
    return delete_user(id_persona)

@router.patch("/{id_persona}/estado")
def cambiar_estado_persona(
    id_persona: int,
    data: UpdateEstadoPersonaRequest,
    admin = Depends(require_admin)
):

    return update_estado_persona(
        id_persona,
        data.estado
    )