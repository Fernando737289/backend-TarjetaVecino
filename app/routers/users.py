from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services.user_service import create_user, list_users


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)
def add_user(user: User):
    result = create_user(user)
    if not result:
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    return result

@router.get("/", response_model=list[User])
def get_users():
    return list_users()