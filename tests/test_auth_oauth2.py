from mcp_server.auth_oauth2 import verify_token
from fastapi import Depends
from fastapi.testclient import TestClient
from fastapi import FastAPI
from jose import jwt

app = FastAPI()

@app.get("/verify-oauth2")
def protected_route(token_data=Depends(verify_token)):
    return {"msg": "Success", "data": token_data}


def test_verify_token():
    token = jwt.encode({"sub": "test"}, "secret", algorithm="HS256")
    client = TestClient(app)
    response = client.get("/verify-oauth2", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
