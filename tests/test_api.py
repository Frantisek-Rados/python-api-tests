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