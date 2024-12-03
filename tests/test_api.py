import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(base_url="http://localhost:8002") as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_predict_endpoint():
    async with AsyncClient(base_url="http://localhost:8002") as client:
        payload = {"text": "I love this product!"}
        response = await client.post("/predict", json=payload)
    assert response.status_code == 201
    assert "prediction" in response.json()
