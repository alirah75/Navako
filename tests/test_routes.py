from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome NLP model performs emotion recognition"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["status"] == "Ok"
    assert response_json["details"] == "Model is running ..."
    assert isinstance(response_json["prediction_sample"], list)


def test_predict():
    response = client.post("/predict", json={"sentence": "حال من بسیار خوب است"})
    assert response.status_code == 201
    response_json = response.json()
    assert response_json[0]["label"] == "recommended"
    assert isinstance(response_json[0]["score"], float)
