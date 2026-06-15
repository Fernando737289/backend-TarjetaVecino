# backend-TarjetaVecino

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
DB_PORT=

SECRET_KEY=
FERNET_KEY=

ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

DEC_API_KEY=

URL_API=https://5dev.dec.cl/api/v1/auth/validate_vigencia
```

### Generar SECRET_KEY para JWT

Ejecutar:

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(64))"
```

Copiar el valor generado y asignarlo a:

```env
SECRET_KEY=valor_generado
```

### Generar FERNET_KEY para cifrado de datos sensibles

Ejecutar:

```bash
python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Copiar el valor generado y asignarlo a:

```env
FERNET_KEY=valor_generado
```

### Importante

* No subir el archivo `.env` al repositorio.
* Cada instalación debe generar sus propias claves.
* `SECRET_KEY` se utiliza para la firma y validación de tokens JWT.
* `FERNET_KEY` se utiliza para cifrar datos sensibles como el número de serie de la cédula de identidad.

## Base de datos

Importar el archivo SQL incluido en el proyecto utilizando MySQL o phpMyAdmin.

El script crea automáticamente la base de datos, las tablas y sus relaciones.

## Ejecutar el servicio

```bash
uvicorn main:app --reload
```

Servidor disponible en:

```text
http://127.0.0.1:8000
```

## Documentación Swagger

```text
http://127.0.0.1:8000/docs
```

## Características implementadas

* Autenticación mediante JWT.
* Roles de usuario (`admin` y `funcionario`).
* Protección de rutas mediante token.
* Hash de contraseñas con bcrypt.
* Rate limiting para prevenir ataques de fuerza bruta.
* Validación de vigencia de cédula mediante API externa.
* Cifrado del número de serie de la cédula mediante Fernet.
* Historial de canje de beneficios.
* Auditoría de acciones realizadas en el sistema.

```
```
