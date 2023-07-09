from typing import Any

import jwt

SECRET_KEY = "olympian-tutors-service"
ALGORITHM = "HS256"


def generate_token(email: str) -> str:
    token_data = {"email": email}
    return jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)


def token_verification(token: str) -> Any:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email = payload.get("email")
    print("token verification - email: %s", email)
    if email is None or email == "":
        return ""

    return email
