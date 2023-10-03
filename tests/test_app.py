import pytest
from ..app import app
from flask import session

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert b'Welcome to Flaskpedia!' in response.data

def test_about_route(client):
    response = client.get('/about')
    assert b'About' in response.data

def test_search_route(client):
    response = client.get('/search')
    assert b'Search' in response.data

def test_result_route(client):
    response = client.get('/result')
    assert b'No keyword provided.' in response.data

def test_clear_bookmark_route(client):
    client.get('/clear_bookmark', follow_redirects=True)
    assert session['bookmarks'] == []


