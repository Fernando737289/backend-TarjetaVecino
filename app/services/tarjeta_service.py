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


<<<<<<< HEAD
def create_tarjeta(
    rut: str,
    nombres: str,
    apellidos: str,
    telefono: str | None = None
):
=======
def create_tarjeta(rut: str):
>>>>>>> d346762 (Feature/qr (#13))
    
    try:
        
        persona = get_persona_by_rut(rut)
        
<<<<<<< HEAD
        if persona["nombres"].strip().lower() != nombres.strip().lower():

            raise HTTPException(
                status_code=400,
                detail="Los nombres no coinciden con los registros"
            )

        if persona["apellidos"].strip().lower() != apellidos.strip().lower():

            raise HTTPException(
                status_code=400,
                detail="Los apellidos no coinciden con los registros"
            )
            
        if telefono:
            
            telefono_bd = persona.get("telefono")

            if telefono_bd != telefono:

                raise HTTPException(
                    status_code=400,
                    detail="El teléfono no coincide con los registros"
                )
        
=======
>>>>>>> d346762 (Feature/qr (#13))
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
        
        
<<<<<<< HEAD
def get_tarjeta(rut: str):
=======
def get_tarjeta(id_tarjeta: int):
>>>>>>> d346762 (Feature/qr (#13))
    
    
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
                
<<<<<<< HEAD
            WHERE p.rut = %s
        """
        
        cursor.execute(query, (rut,))
=======
            WHERE t.id_tarjeta = %s
        """
        
        cursor.execute(query, (id_tarjeta,))
>>>>>>> d346762 (Feature/qr (#13))
        
        tarjeta = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if not tarjeta:
            
            raise HTTPException(
                status_code=404,
                detail="Tarjeta no encontrada"
            )
            
<<<<<<< HEAD
        return {
            "nombres": tarjeta["nombres"],
            "apellidos": tarjeta["apellidos"],
            "rut": tarjeta["rut"],
            "numero_tarjeta": tarjeta["numero_tarjeta"],
            "codigo_qr": tarjeta["codigo_qr"],
            "vigencia": tarjeta["fecha_vencimiento"]
        }
=======
        return tarjeta
>>>>>>> d346762 (Feature/qr (#13))
    
    except HTTPException:
        raise
    
    except Exception:
        
        raise HTTPException(
            status_code=500,
            detail="Error al obtener la tarjeta"
        )
        
        
<<<<<<< HEAD
def update_tarjeta(id_tarjeta: int, estado: str, fecha_vencimiento):
    
    try:
        
        conexion = get_connection()
        
        cursor = conexion.cursor(dictionary=True)
        
        query_verificar = """
            SELECT id_tarjeta
            FROM tarjeta
            WHERE id_tarjeta = %s
        """
        
        cursor.execute(
            query_verificar,
            (id_tarjeta,)
        )
        
        tarjeta = cursor.fetchone()
        
        if not tarjeta:
            
            cursor.close()
            conexion.close()
            
            raise HTTPException(
                status_code=404,
                detail="Tarjeta no encontrada"
            )
            
        query_update = """
            UPDATE tarjeta
            SET
                estado = %s,
                fecha_vencimiento = %s
            WHERE id_tarjeta = %s
        """
        
        values = (
            estado,
            fecha_vencimiento,
            id_tarjeta
        )
        
        cursor.execute(query_update, values)
        
        conexion.commit()
        
        cursor.close()
        conexion.close()
        
        return {
            "id_tarjeta": id_tarjeta,
            "mensaje": "Tarjeta actualizada correctamente"
        }
        
    except HTTPException:
        raise
    
    except Exception:
        
        
        raise HTTPException(
            status_code=500,
            detail="Error al actualizar la tarjeta"
        )
        

def delete_tarjeta(id_tarjeta: int):

    try:

        conexion = get_connection()

        cursor = conexion.cursor(dictionary=True)

        query_verificar = """
            SELECT id_tarjeta
            FROM tarjeta
            WHERE id_tarjeta = %s
        """

        cursor.execute(
            query_verificar,
            (id_tarjeta,)
        )

        tarjeta = cursor.fetchone()

        if not tarjeta:

            cursor.close()
            conexion.close()

            raise HTTPException(
                status_code=404,
                detail="Tarjeta no encontrada"
            )

        query_delete = """
            DELETE FROM tarjeta
            WHERE id_tarjeta = %s
        """

        cursor.execute(
            query_delete,
            (id_tarjeta,)
        )

        conexion.commit()

        cursor.close()
        conexion.close()

        return {
            "id_tarjeta": id_tarjeta,
            "mensaje": "Tarjeta eliminada correctamente"
        }

    except HTTPException:
        raise

    except Exception:

        raise HTTPException(
            status_code=500,
             detail="Error al eliminar la tarjeta"
        )
=======
        
>>>>>>> d346762 (Feature/qr (#13))
