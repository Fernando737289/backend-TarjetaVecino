import secrets
import string

def generar_codigo_canje(longitud=20):
    caracteres = string.ascii_uppercase + string.digits
    return "".join(
        secrets.choice(caracteres)
        for _ in range(longitud)
    )