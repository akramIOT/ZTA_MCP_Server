from mcp_server.auth_cert import verify_certificate
from fastapi.testclient import TestClient
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/verify-cert")
def protected_cert_route(request: Request):
    verify_certificate(request)
    return {"msg": "Cert valid"}

def test_cert_auth():
    client = TestClient(app)
    response = client.get("/verify-cert", headers={"X-Client-Cert": "valid_cert"})
    assert response.status_code == 200
