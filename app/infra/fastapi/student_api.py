from fastapi import APIRouter, Depends, File, UploadFile
from pydantic import BaseModel

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core

import aiofiles


class GetStudentResponse(BaseModel):
    first_name: str
    last_name: str
    balance: int
    profile_address: str


class GetLessonResponse(BaseModel):
    subject: str
    tutor_mail: str
    number_of_lessons: int
    lesson_price: int


class ChangeFirstNameRequest(BaseModel):
    new_first_name: str


class ChangeLastNameRequest(BaseModel):
    new_last_name: str


class ChangePasswordRequest(BaseModel):
    new_password: str


class UploadProfilePictureRequest(BaseModel):
    file: UploadFile = File(...)


student_api = APIRouter()


@student_api.get("/student/{student_mail}")
async def get_student(
        student_mail: str,
        core: OlympianTutorService = Depends(get_core),
):
    print("/student/" + student_mail)

    student = core.get_student(student_mail)
    response = GetStudentResponse(
        first_name=student.first_name,
        last_name=student.last_name,
        balance=student.balance,
        profile_address=student.profile_address,
    )

    return response


@student_api.get("/student/lessons/{student_mail}")
async def get_student_lessons(
        student_mail: str,
        core: OlympianTutorService = Depends(get_core),
):
    print("/student/lessons/" + student_mail)

    lessons = core.student_interactor.get_student_lessons(student_mail)
    responses = []
    for lesson in lessons:
        print(lesson)
        response = GetLessonResponse(
            subject=lesson.subject,
            tutor_mail=lesson.tutor_mail,
            number_of_lessons=lesson.number_of_lessons,
            lesson_price=lesson.lesson_price,
        )
        responses.append(response)

    return responses


@student_api.post("/student/change_first_name/{student_mail}")
async def change_first_name(
        data: ChangeFirstNameRequest,
        student_mail: str,
        core: OlympianTutorService = Depends(get_core),
):
    print("/student/change_first_name/" + student_mail + " value: " + data.new_first_name)

    student = core.get_student(student_mail)
    core.change_student_first_name(student_mail, data.new_first_name)

    return {"message": "Changed student first name successfully."}


@student_api.post("/student/change_last_name/{student_mail}")
async def change_last_name(
        data: ChangeLastNameRequest,
        student_mail: str,
        core: OlympianTutorService = Depends(get_core),
):
    print("/student/change_last_name/" + student_mail + " value: " + data.new_last_name)

    student = core.get_student(student_mail)
    core.change_student_last_name(student_mail, data.new_last_name)

    return {"message": "Changed student last name successfully."}


@student_api.post("/student/change_password/{student_mail}")
async def change_password(
        data: ChangePasswordRequest,
        student_mail: str,
        core: OlympianTutorService = Depends(get_core),
):
    print("/student/change_password/" + student_mail + " value: " + data.new_password)

    student = core.get_student(student_mail)
    core.change_student_password(student_mail, data.new_password)

    return {"message": "Changed student password successfully."}


@student_api.post("/student/upload_profile_picture/{student_mail}")
async def create_upload_file(
        student_mail: str,
        file: UploadFile = File(...),
        core: OlympianTutorService = Depends(get_core),
):
    dest_path = '../../frontend/src/Storage/' + student_mail
    async with aiofiles.open(dest_path, 'wb') as dest_file:
        content = await file.read()
        await dest_file.write(content)

    core.change_student_profile_address(student_mail, dest_path)
