import json
import pytest

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    yield client

def test_create_note(client):
    response = client.post(
        '/notes',
        data=json.dumps({'title': 'Test Title', 'content': 'Test Content'}),
        content_type='application/json'
    )
    assert response.status_code == 201
    assert json.loads(response.data) == {'id': 1, 'title': 'Test Title', 'content': 'Test Content'}

def test_get_note(client):
    response = client.get('/notes/1')
    assert response.status_code == 200
    assert json.loads(response.data) == {'id': 1, 'title': 'Test Title', 'content': 'Test Content'}

def test_get_notes(client):
    response = client.get('/notes')
    assert response.status_code == 200
    assert json.loads(response.data) == [{'id': 1, 'title': 'Test Title', 'content': 'Test Content'}]

def test_update_note(client):
    response = client.put(
        '/notes/1',
        data=json.dumps({'title': 'New Title', 'content': 'New Content'}),
        content_type='application/json'
    )
    assert response.status_code == 200
    assert json.loads(response.data) == {'id': 1, 'title': 'New Title', 'content': 'New Content'}

def test_delete_note(client):
    response = client.delete('/notes/1')
    assert response.status_code == 204
