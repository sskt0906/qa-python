import pytest
import requests

BASE_URL = "https://httpbin.org"
TIMEOUT = 30

def assert_status_code(response, expected_status_code):
    if response.status_code == 503:
        pytest.skip("外部APIが503を返したためスキップ")

    assert response.status_code == expected_status_code

def test_get_api_status_code():
    response = requests.get(f"{BASE_URL}/get", timeout=TIMEOUT)

    assert_status_code(response, 200)


def test_get_api_json():
    response = requests.get(f"{BASE_URL}/get", timeout=TIMEOUT)

    assert_status_code(response, 200)

    data = response.json()

    assert "url" in data
    assert data["url"] == f"{BASE_URL}/get"


def test_post_api_json():
    payload = {
        "name": "sasaki",
        "job": "qa"
    }

    response = requests.post(
        f"{BASE_URL}/post",
        json=payload,
        timeout=TIMEOUT
    )

    assert_status_code(response, 200)

    data = response.json()

    assert data["json"]["name"] == payload["name"]
    assert data["json"]["job"] == payload["job"]


def test_not_found_status_code():
    response = requests.get(f"{BASE_URL}/status/404", timeout=TIMEOUT)

    assert_status_code(response, 404)


def test_server_error_status_code():
    response = requests.get(f"{BASE_URL}/status/500", timeout=TIMEOUT)

    assert_status_code(response, 500)


@pytest.mark.parametrize("status_code", [200, 404, 500])
def test_status_code_parametrize(status_code):
    response = requests.get(
        f"{BASE_URL}/status/{status_code}",
        timeout=TIMEOUT
    )

    assert_status_code(response, status_code)