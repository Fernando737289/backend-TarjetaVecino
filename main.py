from fastapi import FastAPI
from app.routers import db_conection, users


app = FastAPI(title="Mi API")

app.include_router(users.router)
app.include_router(db_conection.router)

@app.get("/")
def read_root():
    return {"msg": "Bienvenido a la API"}