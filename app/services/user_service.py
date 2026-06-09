from app.core.database import get_connection
from fastapi import HTTPException
from app.services.dec_services import validar_vigencia_rut

async def create_user(user):
    try:
        
        resultado_dec = await validar_vigencia_rut(
            user_rut=user.rut,
            serial_number=user.serial_number  
        )
        
       
        if not resultado_dec or resultado_dec.get("status") != 200:
            raise HTTPException(
                status_code=400, 
                detail="No se pudo verificar la cédula con el servicio externo."
            )
            
        result_data = resultado_dec.get("result", {})
        if result_data.get("Verificacion") != "V":
            raise HTTPException(
                status_code=400, 
                detail="La cédula de identidad no se encuentra vigente en el Registro Civil."
            )
    
        conexion = get_connection()
        
        cursor = conexion.cursor(dictionary=True)
        
        query = """
            INSERT INTO persona (
                rut,
                nombres,
                apellidos,
                direccion,
                numero_direccion,
                telefono,
                email,
                fecha_nacimiento
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        values = (
            user.rut,
            user.nombres,
            user.apellidos,
            user.direccion,
            user.numero_direccion,
            user.telefono,
            user.email,
            user.fecha_nacimiento
        )
        
        cursor.execute(query, values)
        
        conexion.commit()
        
        return {"status": "success", "message": "Persona creada exitosamente tras validación de cédula."}
        
    except HTTPException as http_err:
        
        raise http_err
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error interno al registrar en la base de datos: {str(e)}"
        )
    finally:

        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


def list_users():
    
    try:
    
        conexion = get_connection()
    
        cursor = conexion.cursor(dictionary=True)
    
        query = "SELECT * FROM persona"
    
        cursor.execute(query)
    
        resultado = cursor.fetchall()
    
        cursor.close()
        conexion.close()
    
        return resultado
    
    except Exception:
        
        raise HTTPException(
            status_code = 500,
            detail = "Error al obtener personas"
        )

    
def update_user(id_persona, user):
    
    try:
        
        conexion = get_connection()
    
        cursor = conexion.cursor(dictionary=True)
        
        query = """
            UPDATE persona
            SET
                rut = %s,
                nombres = %s,
                apellidos = %s,
                direccion = %s,
                numero_direccion = %s,
                telefono = %s,
                email = %s,
                fecha_nacimiento = %s
            WHERE id_persona = %s
        """
        
        values = (
            user.rut,
            user.nombres,
            user.apellidos,
            user.direccion,
            user.numero_direccion,
            user.telefono,
            user.email,
            user.fecha_nacimiento,
            id_persona
        )
        
        cursor.execute(query, values)
        
        conexion.commit()
        
        if cursor.rowcount == 0:
            
            raise HTTPException(
                status_code = 404,
                detail = "Usuario no encontrado"
            )
        
        cursor.close()
        conexion.close()
        
        return {
            "mensaje": "Usuario actualizado correctamente"
        }
    
    except HTTPException:
        raise
    
    except Exception:
        
        raise HTTPException(
            status_code = 500,
            detail = "Error al actualizar usuario"
        )

     
def delete_user(id_persona):
    
    try:

        conexion = get_connection()
    
        cursor = conexion.cursor(dictionary=True)
        
        query = """
            DELETE FROM persona
            WHERE id_persona = %s
        """
        
        cursor.execute(query, (id_persona,))
        
        conexion.commit()
        
        if cursor.rowcount == 0:
            
            raise HTTPException(
                status_code = 404,
                detail = "Usuario no encontrado"
            )
            
        cursor.close()
        conexion.close()
        
        return {
            "mensaje": "Usuario eliminado correctamente"
        }
        
    except HTTPException:
        raise
    
    except Exception:
        
        raise HTTPException(
            status_code = 500,
            detail = "Error al eliminar usuario"
        )
        