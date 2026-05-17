# backend-TarjetaVecino

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto con las credenciales de la base de datos:

```env
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
DB_PORT=
```

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