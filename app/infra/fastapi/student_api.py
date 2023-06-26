import smtplib
import ssl

import aiofiles
from fastapi import APIRouter, Depends, File, UploadFile
from pydantic import BaseModel

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core


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

class MessageToTutorRequest(BaseModel):
    message_text: str
    tutor_mail: str
    student_mail: str

class ChangeFirstNameRequest(BaseModel):
    new_first_name: str


class ChangeLastNameRequest(BaseModel):
    new_last_name: str


class ChangePasswordRequest(BaseModel):
    new_password: str


class UploadProfilePictureRequest(BaseModel):
    file: UploadFile = File(...)


class ReportToAdminRequest(BaseModel):
    report: str


class AddBalanceRequest(BaseModel):
    amount: int


class FinishHomeworkRequest(BaseModel):
    homework_text: str
    tutor_mail: str
    student_mail: str


class BuyLessonRequest(BaseModel):
    subject: str
    tutor_mail: str
    lesson_price: int


student_api = APIRouter()


@student_api.get("/student/{student_mail}")
async def get_student(
    student_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    print("/student/" + student_mail)

    student = core.student_interactor.get_student(student_mail)
    response = GetStudentResponse(
        first_name=student.first_name,
        last_name=student.last_name,
        balance=student.balance,
        profile_address=student.profile_address,
    )

    return response


@student_api.get("/student/messaged_tutors/{student_mail}")
async def get_student_messaged_tutors(
    student_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    print("/student/" + student_mail)

    student_messaged_tutors = core.message_interactor.get_student_messaged_tutors(student_mail)
    print(student_messaged_tutors)
    return student_messaged_tutors


@student_api.get("/student/homeworks/{student_mail}")
async def get_student_homeworks(
    student_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    homeworks = core.homework_interactor.get_student_homework(student_mail)
    return homeworks


@student_api.get("/student/lessons/{student_mail}")
async def get_student_lessons(
    student_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    print("/student/lessons/" + student_mail)

    lessons = core.student_interactor.get_student_lessons(student_mail)
    responses = []
    for lesson in lessons:
        response = GetLessonResponse(
            subject=lesson.subject,
            tutor_mail=lesson.tutor_mail,
            number_of_lessons=lesson.number_of_lessons,
            lesson_price=lesson.lesson_price,
        )
        responses.append(response)

    return responses


@student_api.get("/student/messages/{student_mail}/{tutor_mail}")
async def get_student_lessons(
    student_mail: str,
    tutor_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    print("/student/lessons/" + student_mail)

    messages = core.message_interactor.get_messages(tutor_mail,student_mail)
    print(messages)
    return messages
@student_api.post("/student/change_first_name/{student_mail}")
async def change_first_name(
    data: ChangeFirstNameRequest,
    student_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    print(
        "/student/change_first_name/" + student_mail + " value: " + data.new_first_name
    )

    student = core.student_interactor.get_student(student_mail)
    core.student_interactor.change_student_first_name(student_mail, data.new_first_name)

    return {"message": "Changed student first name successfully."}





@student_api.post("/student/message_to_tutor")
async def change_first_name(
    data: MessageToTutorRequest,
    core: OlympianTutorService = Depends(get_core),
):

    message_text = data.message_text
    tutor_mail = data.tutor_mail
    student_mail = data.student_mail
    student = core.student_interactor.get_student(student_mail)
    tutor =core.tutor_interactor.get_tutor(tutor_mail)
    if student is None:
        return {"message":"Student with this visitor mail doesn't exits"}
    if tutor is None:
        return {"message":"Tutor with this mail doesn't exist."}
    core.message_interactor.create_message(message_text,tutor_mail,student_mail)
    return {"message": "Message sent successfully."}


@student_api.delete("/student/finish_homework")
async def finish_homework(
    finish_homework: FinishHomeworkRequest,
    core: OlympianTutorService = Depends(get_core),
):
    print(finish_homework)
    homework_text = finish_homework.homework_text
    tutor_mail = finish_homework.tutor_mail
    student_mail = finish_homework.student_mail
    core.homework_interactor.delete_homework(homework_text, tutor_mail, student_mail)
    return {"message": "Homework finished successfully."}


@student_api.post("/student/change_last_name/{student_mail}")
async def change_last_name(
    data: ChangeLastNameRequest,
    student_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    print("/student/change_last_name/" + student_mail + " value: " + data.new_last_name)

    student = core.student_interactor.get_student(student_mail)
    core.student_interactor.change_student_last_name(student_mail, data.new_last_name)

    return {"message": "Changed student last name successfully."}


@student_api.post("/student/change_password/{student_mail}")
async def change_password(
    data: ChangePasswordRequest,
    student_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    print("/student/change_password/" + student_mail + " value: " + data.new_password)

    student = core.student_interactor.get_student(student_mail)
    core.student_interactor.change_student_password(student_mail, data.new_password)

    return {"message": "Changed student password successfully."}


@student_api.post("/student/upload_profile_picture/{student_mail}")
async def create_upload_file(
    student_mail: str,
    file: UploadFile = File(...),
    core: OlympianTutorService = Depends(get_core),
):
    dest_path = "../../frontend/src/Storage/" + student_mail
    async with aiofiles.open(dest_path, "wb") as dest_file:
        content = await file.read()
        await dest_file.write(content)

    core.student_interactor.change_student_profile_address(student_mail, dest_path)


@student_api.post("/student/add_balance/{student_mail}")
async def add_balance(
    student_mail: str,
    data: AddBalanceRequest,
):
    print("/student/add_balance/" + student_mail)
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "tutorsite727@gmail.com"
    password = "fvqxtupjruxqcooo"
    message = student_mail + " [add_balance] " + str(data.amount)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(student_mail, sender_email, message)

    return {"message": "Sent a balance increase message to admin."}


@student_api.post("/student/buy_lesson/{student_mail}")
async def buy_lesson(
    student_mail: str,
    data: BuyLessonRequest,
    core: OlympianTutorService = Depends(get_core),
):
    student_balance = core.student_interactor.get_student_balance(student_mail)
    if student_balance >= data.lesson_price:
        lesson = core.lesson_interactor.get_lesson(
            data.tutor_mail, student_mail, data.subject
        )
        if lesson is None:
            core.lesson_interactor.create_lesson(
                data.subject, data.tutor_mail, student_mail, 1, data.lesson_price
            )
        else:
            core.lesson_interactor.set_number_of_lessons(
                data.tutor_mail,
                student_mail,
                lesson.number_of_lessons + 1,
                data.subject,
            )

        core.student_interactor.set_student_balance(
            student_mail, student_balance - data.lesson_price
        )
        print("Bought a lesson successfully")
        return {"message": "Bought a lesson successfully."}
    else:
        print("Could not buy a lesson because of insufficient balance")
        return {"message": "Could not buy a lesson because of insufficient balance."}
