import requests

def test_get_api_status_code():
    response = requests.get("https://httpbin.org/get", timeout=10)

    assert response.status_code == 200

def test_get_api_json():
    response = requests.get("https://httpbin.org/get", timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert "url" in data
    assert data["url"] == "https://httpbin.org/get"

def test_post_api_json():
    payload = {
        "name": "sasaki",
        "job": "qa"
    }

    response = requests.post(
        "https://httpbin.org/post",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["json"]["name"] == "sasaki"
    assert data["json"]["job"] == "qa"

def test_not_found_status_code():
    response = requests.get("https://httpbin.org/status/404", timeout=10)

    assert response.status_code == 404

def test_server_error_status_code():
    response = requests.get("https://httpbin.org/status/500", timeout=10)

    assert response.status_code == 500

import pytest

@pytest.mark.parametrize("status_code", [200, 404, 500])
def test_status_code_parametrize(status_code):
    response = requests.get(
        f"https://httpbin.org/status/{status_code}",
        timeout=10
    )

    assert response.status_code == status_code