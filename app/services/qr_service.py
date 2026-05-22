import qrcode
from io import BytesIO

from fastapi import HTTPException
from app.core.database import get_connection


def get_persona_by_rut(rut: str):
    
    try:
        
        conexion = get_connection()
        
        cursor = conexion.cursor(dictionary=True)
        
        query = """
            SELECT
                rut,
                nombres,
                apellidos
            FROM persona
            WHERE rut = %s
        """
        
        cursor.execute(query, (rut,))
        
        persona = cursor.fetchone()
        
        
        if not persona:
            raise HTTPException(
                status_code=404,
                detail="Persona no encontrada"
            )
        
        return persona
    
    except HTTPException:
        raise
    
    except Exception:
        
        raise HTTPException(
            status_code=500,
            detail="Error al buscar persona"
        )


def generar_qr(persona):
    
    contenido = f"""
    Rut: {persona['rut']}
    Nombre: {persona['nombres']}
    Apellidos: {persona['apellidos']}
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
        
    qr.add_data(contenido)
    
    qr.make(fit=True)
    
    imagen_qr = qr.make_image(
        fill_color = "black",
        back_color = "white"
    )
    
    buffer = BytesIO()
    
    imagen_qr.save(buffer, format="PNG")
    
    buffer.seek(0)
    
    return buffer