from fastapi import Request, HTTPException

def verify_certificate(request: Request):
    cert = request.headers.get("X-Client-Cert")
    if not cert or cert != "valid_cert":  # replace with real cert logic
        raise HTTPException(status_code=403, detail="Invalid or missing client certificate")
    return True
