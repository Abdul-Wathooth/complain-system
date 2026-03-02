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

def test_add_complaint(client):
    response = client.post('/complaint', json={"name":"Abdul","issue":"Server down"})
    assert response.status_code == 201

# 🔹 New: Test get complaints
def test_get_complaints(client):
    # Add a complaint first
    client.post('/complaint', json={"name":"Abdul","issue":"Server down"})
    response = client.get('/complaints')
    data = response.get_json()
    assert isinstance(data, list)
    assert {"name":"Abdul","issue":"Server down"} in data
