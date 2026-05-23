from fastapi import APIRouter
from app.models.user import User
from app.services.user_service import create_user, list_users, update_user, delete_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

#ruta crud para persona
@router.get("/")
def list_all_users():
    return list_users()

@router.post("/crear")
def create_new_user(user: User):
    return create_user(user)

@router.put("/{id_persona}")
def update_users(id_persona: int, user: User):
    return update_user(id_persona, user)

@router.delete("/{id_persona}")
def delete_users(id_persona: int):
    return delete_user(id_persona)