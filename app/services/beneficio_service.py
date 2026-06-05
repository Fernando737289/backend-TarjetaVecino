from fastapi import HTTPException 
from app.core.database import get_connection


def create_beneficio(data):

    try:

        conexion = get_connection()

        cursor = conexion.cursor(dictionary=True)

        query = """
            INSERT INTO beneficios(
                nombre,
                descripcion,
                tipo_descuento,
                valor_descuento,
                stock,
                fecha_inicio,
                fecha_vencimiento,
                comercio
            )
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            data.nombre,
            data.descripcion,
            data.tipo_descuento,
            data.valor_descuento,
            data.stock,
            data.fecha_inicio,
            data.fecha_vencimiento,
            data.comercio
        )

        cursor.execute(query, values)

        conexion.commit()

        id_beneficio = cursor.lastrowid

        cursor.close()
        conexion.close()

        return {
            "id_beneficio": id_beneficio,
            "mensaje": "Beneficio creado correctamente"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


def list_beneficios():

    try:

        conexion = get_connection()

        cursor = conexion.cursor(dictionary=True)

        query = """
            SELECT *
            FROM beneficios
            WHERE estado = 'activo'
        """

        cursor.execute(query)

        beneficios = cursor.fetchall()

        cursor.close()
        conexion.close()

        return beneficios

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Error al obtener beneficios"
        )