from app.core.database import get_connection


def registrar_auditoria(
         id_auditoria
         tabla_afectada
         accion_realizada
         descripcion
         usuario_accion
         fecha_accion
):

    conexion = get_connection()

    cursor = conexion.cursor()

    query = """
        INSERT INTO auditoria(
            id_auditoria
            tabla_afectada
            accion_realizada
            descripcion
            usuario_accion
            fecha_accion
        )
        VALUES(%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            id_auditoria
            tabla_afectada
            accion_realizada
            descripcion
            usuario_accion
            fecha_accion
        )
    )

    conexion.commit()

    cursor.close()
    conexion.close()