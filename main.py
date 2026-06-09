from fastapi import FastAPI
from app.routers import (
    db_conection,
    users,
    qr_router,
    tarjeta_router,
    beneficio_router
    verificacion_router
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mi API")

app.include_router(users.router)
app.include_router(db_conection.router)
app.include_router(qr_router.router)
app.include_router(tarjeta_router.router)
app.include_router(beneficio_router.router)
app.include_router(verificacion_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"msg": "Bienvenido a la API"}