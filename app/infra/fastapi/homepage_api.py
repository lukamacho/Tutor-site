from fastapi import APIRouter, Depends
import hashlib
from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core

homepage_api = APIRouter()


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")

    hash_obj = hashlib.sha256(password_bytes)
    password_hash = hash_obj.hexdigest()

    return password_hash


@homepage_api.post("/register")
def create_user(
    is_student: bool,
    mail: str,
    password: str,
    core: OlympianTutorService = Depends(get_core),
):
    hashed_password = hash_password(password)
    print("varegistrireb")
    if is_student:
        core.create_student(email=mail, password=hashed_password)
    else:
        core.create_tutor("", "", mail, hashed_password, 0, "")
