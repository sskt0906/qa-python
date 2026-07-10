from typing import Any

import requests


class UserNotFoundError(Exception):
    """ユーザーが存在しない場合の例外。"""


class InvalidResponseError(Exception):
    """APIレスポンスの内容が不正な場合の例外。"""


class UserApiClient:
    def __init__(
        self,
        base_url: str,
        token: str,
        timeout: int = 5,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            }
        )

    def get_user(self, user_id: int) -> dict[str, Any]:
        """ユーザー情報を取得する。"""

        if user_id <= 0:
            raise ValueError("user_idは1以上で指定してください")

        response = self.session.get(
            f"{self.base_url}/users/{user_id}",
            timeout=self.timeout,
        )

        if response.status_code == 404:
            raise UserNotFoundError(
                f"ユーザーが見つかりません: user_id={user_id}"
            )

        response.raise_for_status()

        data = response.json()
        self._validate_user_response(data)

        return data

    def create_user(
        self,
        name: str,
        job: str,
    ) -> dict[str, Any]:
        """ユーザーを新規登録する。"""

        if not name.strip():
            raise ValueError("nameは必須です")

        if not job.strip():
            raise ValueError("jobは必須です")

        payload = {
            "name": name,
            "job": job,
        }

        response = self.session.post(
            f"{self.base_url}/users",
            json=payload,
            timeout=self.timeout,
        )

        response.raise_for_status()

        if response.status_code != 201:
            raise InvalidResponseError(
                f"期待したステータスは201ですが、"
                f"{response.status_code}が返りました"
            )

        data = response.json()
        self._validate_user_response(data)

        return data

    @staticmethod
    def _validate_user_response(data: dict[str, Any]) -> None:
        """レスポンスに必須項目があるか確認する。"""

        required_fields = {"id", "name", "job"}
        missing_fields = required_fields.difference(data)

        if missing_fields:
            missing_text = ", ".join(sorted(missing_fields))

            raise InvalidResponseError(
                f"レスポンスに必須項目がありません: {missing_text}"
            )