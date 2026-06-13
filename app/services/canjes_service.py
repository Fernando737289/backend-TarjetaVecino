from app.core.database import get_connection
from fastapi import HTTPException, status

async def registrar_canje_seguro(rut_vecino: str, nombre_beneficio: str, descripcion: str):
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)
    
    try:

        query_tarjeta = "SELECT t.id_tarjeta FROM persona p INNER JOIN tarjeta t ON p.id_persona = t.id_persona WHERE p.rut = %s AND t.estado = 'activa'"
        cursor.execute(query_tarjeta, (rut_vecino,))
        tarjeta_vecino = cursor.fetchone()
        
        if not tarjeta_vecino:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Error: El vecino con RUT '{rut_vecino}' no tiene una tarjeta activa registrada en el sistema."
            )
        
        id_tarjeta = tarjeta_vecino['id_tarjeta']

        query_beneficio = "SELECT id_beneficio, id_tarjeta, nombre FROM beneficios WHERE nombre = %s"
        cursor.execute(query_beneficio, (nombre_beneficio,))
        beneficio = cursor.fetchone()
        
        if not beneficio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El beneficio {nombre_beneficio} no existe en el catálogo."
            )
            
        if beneficio['id_tarjeta'] is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error: El beneficio '{beneficio['nombre']}' ya fue cobrado por otra tarjeta y no está disponible."
            )
            

        query_cobrar = """
            UPDATE beneficios 
            SET id_tarjeta = %s, descripcion = %s, estado = 'inactivo'
            WHERE id_beneficio = %s
        """
        cursor.execute(query_cobrar, (id_tarjeta, descripcion, beneficio['id_beneficio']))
        

        query_auditoria = """
            INSERT INTO auditoria (tabla_afectada, accion_realizada, descripcion, usuario_accion)
            VALUES (%s, %s, %s, %s)
        """
        detalle_log = f"Beneficio ID {nombre_beneficio} ('{beneficio['nombre']}') COBRADO por RUT {rut_vecino} (Tarjeta ID {id_tarjeta})"
        cursor.execute(query_auditoria, ("beneficios", "UPDATE", detalle_log, "sistema_backend"))
        
        conexion.commit()
        return {"status": "success", "message": f"¡Beneficio '{beneficio['nombre']}' cobrado con éxito por el vecino RUT {rut_vecino}!"}
        
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno en el servidor: {str(e)}")
    finally:
        cursor.close()
        conexion.close()


async def obtener_vista_historial():
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)
    try:

        query_vista = """
            SELECT 
                b.id_beneficio,
                b.nombre AS nombre_beneficio,
                b.descripcion AS detalle_canje,
                t.numero_tarjeta,
                p.rut AS rut_vecino,
                p.nombres AS nombre_vecino,
                p.apellidos AS apellido_vecino
            FROM beneficios b
            INNER JOIN tarjeta t ON b.id_tarjeta = t.id_tarjeta
            INNER JOIN persona p ON t.id_persona = p.id_persona
            ORDER BY b.id_beneficio DESC
        """
        cursor.execute(query_vista)
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar el historial relacional: {str(e)}")
    finally:
        cursor.close()
        conexion.close()