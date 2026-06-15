from app.core.database import get_connection
from fastapi import HTTPException


def registrar_uso_beneficio(
    id_persona: int,
    id_beneficio: int
):

    try:

        conexion = get_connection()

        cursor = conexion.cursor()

        query = """
            INSERT INTO historial_beneficios(
                id_persona,
                id_beneficio
            )
            VALUES(%s,%s)
        """

        cursor.execute(
            query,
            (
                id_persona,
                id_beneficio
            )
        )

        conexion.commit()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        cursor.close()
        conexion.close()