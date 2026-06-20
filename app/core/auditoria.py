from app.core.database import get_connection

def registrar_auditoria(
    tabla_afectada: str,
    accion_realizada: str,
    descripcion: str,
    usuario_accion: str
):

    try:

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

    except Exception as e:

        print(f"Error auditoria: {e}")

    finally:

        if 'cursor' in locals():
            cursor.close()

        if 'conexion' in locals():
            conexion.close()

            