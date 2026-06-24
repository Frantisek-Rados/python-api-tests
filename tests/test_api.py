import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data 

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_multiple_posts(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_create_post():
    payload = {"title": "Novy clanok", "body": "Telo clanku", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "Novy clanok"

def test_update_post():
    payload = {"title": "Upraveny clanok"}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Upraveny clanok"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200