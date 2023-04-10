from typing import Callable, Dict

from starlette.testclient import TestClient

from tests.test_api import API_ADMIN_KEY, ErrorMessages


def test_api_error_messages_admin(
    api_client: TestClient, from_msg: Callable[[str], Dict[str, str]]
) -> None:
    response = api_client.get(
        "/admin",
        params={
            API_ADMIN_KEY: "hacker",
        },
    )
    assert response.status_code == ErrorMessages.WRONG_ADMIN_KEY
    assert response.json() == from_msg("Incorrect api key for admin")
