from mcp_server.auth_apikey import verify_api_key
from fastapi.testclient import TestClient
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/verify-apikey")
def protected_key_route(request: Request):
    verify_api_key(request)
    return {"msg": "API key valid"}

def test_api_key_auth():
    client = TestClient(app)
    response = client.get("/verify-apikey", headers={"X-API-Key": "123456"})
    assert response.status_code == 200
