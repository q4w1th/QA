import requests

from conftest import base_url

def test_get_post_returns_200():
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200

def test_post_has_required_fields():
    response = requests.get(f"{base_url}/posts/1")
    data = response.json()
    assert "userId" in data
    assert "title" in data
    assert "body" in data

def test_nonexistent_post_returns_404():
    response = requests.get(f"{base_url}/posts/999")
    assert response.status_code == 404

def test_create_post():
    new_post = {
        "userId": 1,
        "title": "мой первый тест",
        "body": "автоматизация это круто"
    }
    response = requests.post(
        f"{base_url}/posts",
        json=new_post
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "мой первый тест"
    assert "id" in data