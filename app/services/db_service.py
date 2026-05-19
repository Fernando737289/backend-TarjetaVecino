from app.core.database import get_connection

#prueba de conexion a base de datos.
def database_connection():
    
    try:
        
        conexion = get_connection()
        
        cursor = conexion.cursor()
        
        cursor.execute("SELECT DATABASE();")
        
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        return {
            "conexion": "exitosa",
            "baseDeDatos": resultado[0]
        }
    
    except Exception as error:
        
        return {
            
            "error": str(error)
        }
