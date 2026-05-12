from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="Mi API de Usuarios")

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"msg": "Bienvenido a la API"}