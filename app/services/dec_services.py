from pydantic import BaseModel
import httpx
from fastapi import HTTPException, status

URL_DEC = "https://5dev.dec.cl/api/v1/auth/validate_vigencia"

async def validar_vigencia_rut(user_rut: str, serial_number: str, api_key: str) -> dict:
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "user_rut": user_rut,
        "serial_number": serial_number
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(URL_DEC, headers=headers, json=payload, timeout=10.0)
            
            response.raise_for_status()
            
            return response.json()
            
        except httpx.HTTPStatusError as e:
            
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f"Error en el servicio externo de validación: {e.response.text}"
            )
        except httpx.RequestError:
            
            raise HTTPException(
                status_code=status.HTTP_500_SERVICE_UNAVAILABLE,
                detail="El servicio externo de validación no se encuentra disponible temporalmente."
            )