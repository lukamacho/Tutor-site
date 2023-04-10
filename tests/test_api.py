from fastapi.testclient import TestClient

from app.core.admin.admin import ADMIN_KEY

API_ADMIN_KEY = "admin_key"
API_ARG_KEY_NAME = "api_key"
class ErrorMessages:
    OK = 200

    API_ENDPOINT_NOT_FOUND = 404
    USER_NOT_FOUND = 410
    BALANCE_NOT_FOUND = 411
    NO_MORE_LESSONS = 412
    NO_SUCH_COURSE = 413
    UNAUTHORIZED = 414
    NO_SUCH_SUBJECT = 415
    NO_MORE_MONEY = 416
    WRONG_ADMIN_KEY = 417
    ALREADY_TOP_TUTOR = 418