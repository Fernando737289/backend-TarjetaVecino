from fastapi import HTTPException
from app.core.database import get_connection


def registrar_auditoria(
    tabla_afectada: str,
    accion_realizada: str,
    descripcion: str,
    usuario_accion: str
):

    conexion = get_connection()

    cursor = conexion.cursor()

    query = """
        INSERT INTO auditoria(
            tabla_afectada,
            accion_realizada,
            descripcion,
            usuario_accion
        )
        VALUES(%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            tabla_afectada,
            accion_realizada,
            descripcion,
            usuario_accion
        )
    )

    conexion.commit()

    cursor.close()
    conexion.close()
    

def list_auditoria():

    try:

        conexion = get_connection()

        cursor = conexion.cursor(dictionary=True)

        query = """
            SELECT
                tabla_afectada,
                accion_realizada,
                descripcion,
                usuario_accion,
                fecha_accion
            FROM auditoria
            ORDER BY fecha_accion DESC
        """

        cursor.execute(query)

        resultado = cursor.fetchall()

        cursor.close()
        conexion.close()

        return resultado

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Error al obtener auditoría"
        )
