from fastapi import HTTPException

from app.core.database import get_connection
from app.core.security import (
    verify_password,
    create_access_token
)


def login_user(
    email: str,
    password: str
):
    
    conexion = get_connection()
    
    cursor = conexion.cursor(dictionary=True)
    
    query = """
        SELECT
            id_usuario,
            username,
            password_hash,
            rol,
            estado,
            email
        FROM usuario
        WHERE email = %s
    """
    
    cursor.execute(
        query,
        (email,)
    )
    
    usuario = cursor.fetchone()
    
    cursor.close()
    conexion.close()
    
    if not usuario:
        
        raise HTTPException(
            status_code = 401,
            detail= "Credenciales invalidas"
        )
        
    if usuario["estado"] != "activo":
        
        raise HTTPException(
            status_code=401,
            detail="Usuario inactivo"
        )
        
    if not verify_password(
        password,
        usuario["password_hash"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Credenciales invalidas"
        )
        
    token = create_access_token({
        "sub": usuario["username"],
        "id_usuario": usuario["id_usuario"],
        "rol": usuario["rol"]
    })
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }