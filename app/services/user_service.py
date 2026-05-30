from app.core.database import get_connection
from fastapi import HTTPException

#crear persona
def create_user(user):
    
    try:
    
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
        
        user_id = cursor.lastrowid
        
        cursor.close()
        conexion.close()
        
        return {
            "id_persona": user_id,
            "mensaje": "Usuario creado correctamente"
        }
        
    except Exception:
        
        raise HTTPException(
            status_code = 500,
            detail = "Error al crear un usuario"
        )

#listar todas las personas.
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

#actualizae persona por su id.     
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

#eliminar persona por su id.      
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
        