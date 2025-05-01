from fastapi import Request, HTTPException
import os

VALID_API_KEYS = os.getenv("VALID_API_KEYS", "123456").split(",")

def verify_api_key(request: Request):
    api_key = request.headers.get("X-API-Key")
    if api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return True
