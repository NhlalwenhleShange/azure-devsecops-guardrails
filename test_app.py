import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'


def test_telemetry(client):
    response = client.get('/api/telemetry')
    assert response.status_code == 200
    assert response.json['device_id'] == 'esp32-sensor-01'
    assert response.json['temperature'] == 24.5
    assert response.json['humidity'] == 60.2
    assert response.json['status'] == 'active'