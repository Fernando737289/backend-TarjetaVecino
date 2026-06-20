from fastapi import Depends
from app.services.auditoria_service import registrar_auditoria
from app.models.user import User
from app.services.user_service import create_user, list_users, update_user, delete_user
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

    resultado = await create_user(payload)

    registrar_auditoria(
        id_usuario=admin["id_usuario"],
        username=admin["sub"],
        accion="CREATE",
        modulo="PERSONA",
        descripcion=f"Creó persona con RUT {payload.rut}"
    )

    return resultado

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

from fastapi import Depends
from app.services.auditoria_service import registrar_auditoria


@router.patch("/{id_persona}/estado")
def cambiar_estado_persona(
    id_persona: int,
    data: UpdateEstadoPersonaRequest,
    usuario = Depends(require_admin)
):

    resultado = update_estado_persona(
        id_persona,
        data.estado
    )

    registrar_auditoria(
        id_usuario=usuario["id_usuario"],
        username=usuario["sub"],
        accion="UPDATE",
        modulo="PERSONA",
        descripcion=f"Cambio estado persona {id_persona} a {data.estado}"
    )

    return resultado
