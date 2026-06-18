from fastapi import HTTPException

from app.core.database import get_connection


def obtener_historial_persona(id_persona: int):

    try:

        conexion = get_connection()
        cursor = conexion.cursor(dictionary=True)

        query = """
            SELECT

                h.codigo_canje,
                h.fecha_uso,

                b.id_beneficio,
                b.nombre,
                b.descripcion,
                b.comercio,
                b.tipo_descuento,
                b.valor_descuento

            FROM historial_beneficios h

            INNER JOIN beneficios b
                ON h.id_beneficio = b.id_beneficio

            WHERE h.id_persona = %s

            ORDER BY h.fecha_uso DESC
        """

        cursor.execute(
            query,
            (id_persona,)
        )

        historial = cursor.fetchall()

        cursor.close()
        conexion.close()

        return historial

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Error al obtener el historial de beneficios"
        )