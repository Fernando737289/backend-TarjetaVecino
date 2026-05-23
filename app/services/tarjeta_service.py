import random
from app.core.database import get_connection
from datetime import date, timedelta
from fastapi import HTTPException

from app.services.qr_service import (
    get_persona_by_rut,
    generar_qr
)


def verificar_tarjeta_existente(id_persona: int):

    conexion = get_connection()

    cursor = conexion.cursor(dictionary=True)

    query = """
        SELECT id_tarjeta
        FROM tarjeta
        WHERE id_persona = %s
    """

    cursor.execute(query, (id_persona,))

    tarjeta = cursor.fetchone()

    cursor.close()
    conexion.close()

    return tarjeta


def create_tarjeta(rut: str):
    
    try:
        
        persona = get_persona_by_rut(rut)
        
        tarjeta_existente = verificar_tarjeta_existente(
            persona["id_persona"]
        )
        
        if tarjeta_existente:
            
            raise HTTPException(
                status_code=400,
                detail="La persona ya posee una tarjeta"
            )
            
        codigo_qr = generar_qr(persona)
        
        numero_tarjeta = f"{random.randint(100000,999999)}"
        
        fecha_emision = date.today()
        
        fecha_vencimiento = fecha_emision + timedelta(days=365)
        
        conexion = get_connection()
        
        cursor = conexion.cursor(dictionary=True)
        
        query = """
            INSERT INTO tarjeta(
                id_persona,
                numero_tarjeta,
                codigo_qr,
                fecha_emision,
                fecha_vencimiento,
                estado
            )
            VALUES(%s,%s,%s,%s,%s,%s)
        """

        values = (
            persona["id_persona"],
            numero_tarjeta,
            codigo_qr,
            fecha_emision,
            fecha_vencimiento,
            "activa"
        )
        
        cursor.execute(query, values)

        conexion.commit()
        
        id_tarjeta = cursor.lastrowid
        
        cursor.close()
        conexion.close()
        
        return {
            "id_tarjeta": id_tarjeta,
            "mensaje": "Tarjeta creada correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Error al crear tarjeta: {str(e)}"
        )
        
        
def get_tarjeta(id_tarjeta: int):
    
    
    try:
        
        conexion = get_connection()
        
        cursor = conexion.cursor(dictionary=True)
        
        query = """
            SELECT
                t.id_tarjeta,
                t.numero_tarjeta,
                t.codigo_qr,
                t.fecha_emision,
                t.fecha_vencimiento,
                t.estado,

                p.rut,
                p.nombres,
                p.apellidos,
                p.telefono
            
            FROM tarjeta t
            
            INNER JOIN persona p
                ON t.id_persona = p.id_persona
                
            WHERE t.id_tarjeta = %s
        """
        
        cursor.execute(query, (id_tarjeta,))
        
        tarjeta = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if not tarjeta:
            
            raise HTTPException(
                status_code=404,
                detail="Tarjeta no encontrada"
            )
            
        return tarjeta
    
    except HTTPException:
        raise
    
    except Exception:
        
        raise HTTPException(
            status_code=500,
            detail="Error al obtener la tarjeta"
        )
        
        
        