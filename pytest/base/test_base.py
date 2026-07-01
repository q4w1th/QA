import requests

def test_get_post_returns_200(api_url):
    response = requests.get(f"{api_url}/posts/1")
    assert response.status_code == 200

def test_posts_has_required_fields(api_url):
    response = requests.get(f"{api_url}/posts/1")
    data = response.json()
    assert "userId" in data
    assert "title" in data
    assert "body" in data

def test_nonexistent_post_returns_404(api_url):
    response = requests.get(f"{api_url}/posts/999")
    assert response.status_code == 404

def test_create_post(api_url):
    new_post = {
        "userId": 1,
        "title": "мой первый тест",
        "body": "автоматизация это круто"
    }
    response = requests.post(
        f"{api_url}/posts",
        json=new_post
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "мой первый тест"
    assert "id" in data

def test_get_users_returns_200(api_url):
    response = requests.get(f"{api_url}/users/1")
    assert response.status_code == 200

def test_users_has_required_fields(api_url):
    response = requests.get(f"{api_url}/users/1")
    data = response.json()
    assert "name" in data
    assert "email" in data
    assert "phone" in data