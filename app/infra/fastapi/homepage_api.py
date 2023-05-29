from fastapi import APIRouter, Depends
import hashlib
from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core
from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    mail: str
    password: str
    is_student: bool


homepage_api = APIRouter()


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")

    hash_obj = hashlib.sha256(password_bytes)
    password_hash = hash_obj.hexdigest()

    return password_hash


@homepage_api.post("/sign_up")
async def create_user(
    data: CreateUserRequest, core: OlympianTutorService = Depends(get_core)
):
    password_hash = hash_password(data.password)

    if data.is_student:
        student_mail = data.mail
        student = core.tutor_interactor.get_tutor(student_mail)
        if student is None:
            return {"message": "Student with this mail doesn't exist!"}
        core.create_student(
            data.first_name, data.last_name, data.mail, password_hash, 0
        )
        return {"message": {"Student added successfully."}}
    else:
        tutor_mail = data.mail
        tutor = core.tutor_interactor.get_tutor(tutor_mail)
        if tutor is not None:
            return {"message": "Tutor with this mail already exists!"}
        core.create_tutor(
            data.first_name, data.last_name, data.mail, password_hash, 0, ""
        )
        return {"message": {"Tutor added successfully."}}
