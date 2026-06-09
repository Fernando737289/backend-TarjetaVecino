import bcrypt

from fastapi import HTTPException
from app.core.database import get_connection


def create_usuario(data):

    try:

        conexion = get_connection()
        cursor = conexion.cursor(dictionary=True)

        query_verificar = """
            SELECT id_usuario
            FROM usuario
            WHERE usuario = %s
               OR correo = %s
        """

        cursor.execute(
            query_verificar,
            (data.usuario, data.correo)
        )

        existe = cursor.fetchone()

        if existe:

            raise HTTPException(
                status_code=400,
                detail="Usuario o correo ya registrado"
            )

        password_hash = bcrypt.hashpw(
            data.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        query = """
            INSERT INTO usuario(
                usuario,
                correo,
                password_hash
            )
            VALUES(%s,%s,%s)
        """

        values = (
            data.usuario,
            data.correo,
            password_hash
        )

        cursor.execute(query, values)

        conexion.commit()

        id_usuario = cursor.lastrowid

        cursor.close()
        conexion.close()

        return {
            "id_usuario": id_usuario,
            "mensaje": "Usuario creado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
