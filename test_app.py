import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_webhook_route(client):
    response = client.post('/webhook', json={"test": "hello"})
    assert response.status_code == 200
