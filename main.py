from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from app.routers.canjes_router import router as canjes_router

from app.routers import (
    db_conection,
    users,
    qr_router,
    tarjeta_router,
    beneficio_router,
    verificacion_router,
    Outh_router,
    auth_router
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mi API")

app.include_router(users.router)
app.include_router(db_conection.router)
app.include_router(qr_router.router)
app.include_router(tarjeta_router.router)
app.include_router(beneficio_router.router)
app.include_router(verificacion_router.router)
app.include_router(Outh_router.router)
app.include_router(auth_router.router)
app.include_router(canjes_router)

limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

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