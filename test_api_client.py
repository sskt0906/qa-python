import pytest
import requests

from api_client import (
    InvalidResponseError,
    UserApiClient,
    UserNotFoundError,
)


BASE_URL = "https://api.example.local"
TOKEN = "secret-token"


@pytest.fixture
def api_client():
    """各テストで使用するAPIクライアント。"""

    return UserApiClient(
        base_url=BASE_URL,
        token=TOKEN,
        timeout=3,
    )


def test_get_user_success(requests_mock, api_client):
    """ユーザー情報を正常に取得できる。"""

    requests_mock.get(
        f"{BASE_URL}/users/1",
        status_code=200,
        json={
            "id": 1,
            "name": "sasaki",
            "job": "qa",
        },
    )

    result = api_client.get_user(1)

    assert result == {
        "id": 1,
        "name": "sasaki",
        "job": "qa",
    }

    # APIが1回だけ呼ばれたか
    assert requests_mock.call_count == 1

    # 実際に送信されたリクエストを確認
    request = requests_mock.last_request

    assert request.method == "GET"
    assert request.url == f"{BASE_URL}/users/1"
    assert request.headers["Authorization"] == f"Bearer {TOKEN}"
    assert request.headers["Accept"] == "application/json"
    assert request.timeout == 3


def test_get_user_not_found(requests_mock, api_client):
    """404なら独自例外を発生させる。"""

    requests_mock.get(
        f"{BASE_URL}/users/999",
        status_code=404,
        json={
            "message": "User not found",
        },
    )

    with pytest.raises(
        UserNotFoundError,
        match="ユーザーが見つかりません",
    ):
        api_client.get_user(999)


def test_get_user_server_error(requests_mock, api_client):
    """500ならrequestsのHTTPErrorを発生させる。"""

    requests_mock.get(
        f"{BASE_URL}/users/1",
        status_code=500,
        json={
            "message": "Internal server error",
        },
    )

    with pytest.raises(requests.exceptions.HTTPError):
        api_client.get_user(1)


def test_get_user_invalid_response(requests_mock, api_client):
    """必須項目が不足しているレスポンスを検知する。"""

    requests_mock.get(
        f"{BASE_URL}/users/1",
        status_code=200,
        json={
            "id": 1,
            "name": "sasaki",
            # jobが存在しない
        },
    )

    with pytest.raises(
        InvalidResponseError,
        match="job",
    ):
        api_client.get_user(1)


def test_get_user_timeout(requests_mock, api_client):
    """タイムアウトが発生した場合の挙動を確認する。"""

    requests_mock.get(
        f"{BASE_URL}/users/1",
        exc=requests.exceptions.ReadTimeout(
            "モックによるタイムアウト"
        ),
    )

    with pytest.raises(requests.exceptions.ReadTimeout):
        api_client.get_user(1)


def test_create_user_success(requests_mock, api_client):
    """ユーザー登録と送信内容を確認する。"""

    requests_mock.post(
        f"{BASE_URL}/users",
        status_code=201,
        json={
            "id": 100,
            "name": "sasaki",
            "job": "qa",
        },
    )

    result = api_client.create_user(
        name="sasaki",
        job="qa",
    )

    assert result["id"] == 100
    assert result["name"] == "sasaki"
    assert result["job"] == "qa"

    request = requests_mock.last_request

    assert request.method == "POST"
    assert request.headers["Authorization"] == f"Bearer {TOKEN}"

    # 実際にPOST送信されたJSONを確認
    assert request.json() == {
        "name": "sasaki",
        "job": "qa",
    }


@pytest.mark.parametrize(
    "name, job, expected_message",
    [
        ("", "qa", "nameは必須です"),
        ("   ", "qa", "nameは必須です"),
        ("sasaki", "", "jobは必須です"),
        ("sasaki", "   ", "jobは必須です"),
    ],
    ids=[
        "empty-name",
        "spaces-only-name",
        "empty-job",
        "spaces-only-job",
    ],
)
def test_create_user_invalid_input(
    requests_mock,
    api_client,
    name,
    job,
    expected_message,
):
    """入力不正ならAPIを呼ばずにエラーにする。"""

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        api_client.create_user(
            name=name,
            job=job,
        )

    # 入力不正なので、API通信は一度も行われない
    assert requests_mock.call_count == 0


@pytest.mark.parametrize(
    "user_id",
    [
        0,
        -1,
    ],
    ids=[
        "zero",
        "negative",
    ],
)
def test_get_user_invalid_id(
    requests_mock,
    api_client,
    user_id,
):
    """不正なIDならAPIを呼ばない。"""

    with pytest.raises(
        ValueError,
        match="user_idは1以上",
    ):
        api_client.get_user(user_id)

    assert requests_mock.call_count == 0
def test_get_user_retry_then_success(
    requests_mock,
    api_client,
):
    """1回目は500、2回目は200なら取得に成功する。"""

    requests_mock.get(
        f"{BASE_URL}/users/1",
        [
            {
                "status_code": 500,
                "json": {
                    "message": "Temporary server error",
                },
            },
            {
                "status_code": 200,
                "json": {
                    "id": 1,
                    "name": "sasaki",
                    "job": "qa",
                },
            },
        ],
    )

    result = api_client.get_user(1)

    assert result == {
        "id": 1,
        "name": "sasaki",
        "job": "qa",
    }

    assert requests_mock.call_count == 2
def test_get_user_retry_then_success(
    requests_mock,
    api_client,
):
    """1回目が500、2回目が200なら取得に成功する。"""

    requests_mock.get(
        f"{BASE_URL}/users/1",
        [
            {
                "status_code": 500,
                "json": {
                    "message": "Temporary server error",
                },
            },
            {
                "status_code": 200,
                "json": {
                    "id": 1,
                    "name": "sasaki",
                    "job": "qa",
                },
            },
        ],
    )

    result = api_client.get_user(1)

    assert result == {
        "id": 1,
        "name": "sasaki",
        "job": "qa",
    }

    assert requests_mock.call_count == 2
def test_get_user_retry_limit_exceeded(
    requests_mock,
    api_client,
):
    """503が続いた場合は、最大回数で打ち切る。"""

    requests_mock.get(
        f"{BASE_URL}/users/1",
        [
            {"status_code": 503},
            {"status_code": 503},
            {"status_code": 503},
        ],
    )

    with pytest.raises(requests.exceptions.HTTPError):
        api_client.get_user(1)

    assert requests_mock.call_count == 3

def test_get_user_timeout_then_success(
    requests_mock,
    api_client,
):
    """1回目がタイムアウト、2回目が200なら成功する。"""

    requests_mock.get(
        f"{BASE_URL}/users/1",
        [
            {
                "exc": requests.exceptions.ReadTimeout(
                    "一時的なタイムアウト"
                )
            },
            {
                "status_code": 200,
                "json": {
                    "id": 1,
                    "name": "sasaki",
                    "job": "qa",
                },
            },
        ],
    )

    result = api_client.get_user(1)

    assert result["id"] == 1
    assert result["name"] == "sasaki"
    assert result["job"] == "qa"

    assert requests_mock.call_count == 2
def test_get_user_404_does_not_retry(
    requests_mock,
    api_client,
):
    """404の場合はリトライせず、1回で終了する。"""

    requests_mock.get(
        f"{BASE_URL}/users/999",
        status_code=404,
        json={
            "message": "User not found",
        },
    )

    with pytest.raises(
        UserNotFoundError,
        match="ユーザーが見つかりません",
    ):
        api_client.get_user(999)

    assert requests_mock.call_count == 1