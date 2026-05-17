from fastapi import APIRouter
from app.services.db_service import database_connection

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/test-db")
def db():
    return database_connection()