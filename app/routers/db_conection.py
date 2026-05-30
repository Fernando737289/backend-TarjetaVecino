from fastapi import APIRouter
from app.services.db_service import database_connection

router = APIRouter(prefix="/health", tags=["Health"])

#ruta de prueba para probar conexion a base de datos
@router.get("/test-db")
def db():
    return database_connection()
