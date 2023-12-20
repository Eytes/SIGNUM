from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_full_statistic():
    response = client.get('/user/full_statistic/123123123')
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_min_statistic():
    response = client.get('/user/min_statistic/123123123')
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
