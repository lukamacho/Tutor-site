import hashlib
import random
import smtplib
import ssl

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.core.facade import OlympianTutorService
from app.infra.fastapi.dependables import get_core


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    mail: str
    password: str
    is_student: bool


class GetCourseResponse(BaseModel):
    subject: str
    tutor_mail: str
    price: int

class GetTutorResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    biography: str
    profile_address: str


homepage_api = APIRouter()


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")

    hash_obj = hashlib.sha256(password_bytes)
    password_hash = hash_obj.hexdigest()

    return password_hash

def send_verification(receiver_mail: str) -> str:
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "tutorsite727@gmail.com"
    password = "fvqxtupjruxqcooo"

    context = ssl.create_default_context()
    verification_text = str(random.randint(0,1000000))

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_mail, verification_text)
    return verification_text

@homepage_api.post("/add_user")
async def add_student(data: CreateUserRequest, core: OlympianTutorService = Depends(get_core)):
    password_hash = hash_password(data.password)
    if data.is_student:
        student_mail = data.mail
        core.student_interactor.create_student(data.first_name,data.last_name,student_mail,password_hash,0)
        return {"message":"Student added successfully."}
    else:
        tutor_mail = data.mail
        core.tutor_interactor.create_tutor(data.first_name, data.last_name,tutor_mail,password_hash,0,"","")
        return {"message":"Tutor added successfully."}




@homepage_api.post("/sign_up")
async def create_user(
        data: CreateUserRequest, core: OlympianTutorService = Depends(get_core)
):
    password_hash = hash_password(data.password)

    if data.is_student:
        student_mail = data.mail
        student = core.student_interactor.get_student(student_mail)
        if student is not None:
            return {"message": "User with this mail already exist!"}
        verification_text = send_verification(student_mail)
        return {"verificationCode": verification_text}
    else:
        tutor_mail = data.mail
        tutor = core.tutor_interactor.get_tutor(tutor_mail)
        if tutor is not None:
            return {"message": "User with this mail already exist!"}
        verification_text = send_verification(tutor_mail)
        return {"verificationCode": verification_text}

    return {"message": "Something unknown happened."}


@homepage_api.get("/courses")
async def get_courses(
        core: OlympianTutorService = Depends(get_core),
):
    print("/courses")

    courses = core.course_interactor.get_courses()
    response = []
    for course in courses:
        response.append(GetCourseResponse(
            subject=course.subject,
            tutor_mail=course.tutor_mail,
            price=course.price
        ))
    return response


@homepage_api.get("/tutors")
async def get_courses(
        core: OlympianTutorService = Depends(get_core),
):
    print("/tutors")

    tutors = core.tutor_interactor.get_tutors()
    response = []
    for tutor in tutors:
        response.append(GetTutorResponse(
            first_name=tutor.first_name,
            last_name=tutor.last_name,
            email=tutor.email,
            biography=tutor.biography,
            profile_address=tutor.profile_address,
        ))
    return response
