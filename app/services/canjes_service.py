from app.core.database import get_connection
from fastapi import HTTPException
from app.core.generador_codigo import generar_codigo_canje

def canjear_beneficio(
    id_persona: int,
    id_beneficio: int
):
    
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    try:

        
        cursor.execute(
            """
            SELECT id_persona
            FROM persona
            WHERE id_persona = %s
            """,
            (id_persona,)
        )

        persona = cursor.fetchone()

        if not persona:
            raise HTTPException(
                status_code=404,
                detail="Persona no encontrada"
            )

        
        cursor.execute(
            """
            SELECT *
            FROM beneficios
            WHERE id_beneficio = %s
            """,
            (id_beneficio,)
        )

        beneficio = cursor.fetchone()

        if not beneficio:
            raise HTTPException(
                status_code=404,
                detail="Beneficio no encontrado"
            )

        
        if beneficio["stock"] <= 0:

            raise HTTPException(
                status_code=400,
                detail="Beneficio sin stock"
            )
            
        cursor.execute(
            """
            SELECT id_historial
            FROM historial_beneficios
            WHERE id_persona = %s
            AND id_beneficio = %s
            """,
            (
                persona["id_persona"],
                id_beneficio
            )
        )

        canje_existente = cursor.fetchone()

        if canje_existente:
            raise HTTPException(
                status_code=400,
                detail="Este beneficio ya fue canjeado por esta persona"
            )
  

        
        cursor.execute(
            """
            UPDATE beneficios
            SET stock = stock - 1
            WHERE id_beneficio = %s
            """,
            (id_beneficio,)
        )
        
        codigo_canje = generar_codigo_canje()

        cursor.execute(
            """
            INSERT INTO historial_beneficios(
                id_persona,
                id_beneficio,
                codigo_canje
            )
            VALUES(%s,%s,%s)
            """,
            (
                persona["id_persona"],
                id_beneficio,
                codigo_canje
            )
        )
                
        conexion.commit()

        return {
            "mensaje": "Beneficio canjeado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)

        )

    finally:

        cursor.close()
        conexion.close()