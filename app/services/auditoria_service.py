from app.core.database import get_connection


def registrar_auditoria(
    id_usuario: int,
    username: str,
    accion: str,
    modulo: str,
    descripcion: str
):

    conexion = get_connection()

    cursor = conexion.cursor()

    query = """
        INSERT INTO auditoria(
            id_usuario,
            username,
            accion,
            modulo,
            descripcion
        )
        VALUES(%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            id_usuario,
            username,
            accion,
            modulo,
            descripcion
        )
    )

    conexion.commit()

    cursor.close()
    conexion.close()