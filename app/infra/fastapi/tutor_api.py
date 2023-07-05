from typing import List

import aiofiles
from fastapi import APIRouter, Depends, File, UploadFile
from pydantic import BaseModel

from app.core.facade import OlympianTutorService
from app.core.student.entity import Student
from app.infra.fastapi.dependables import get_core

tutor_api = APIRouter()


class ChangeBioRequest(BaseModel):
    tutor_mail: str
    new_bio: str


class MoneyWithdrawalRequest(BaseModel):
    tutor_mail: str
    amount: int


class ReviewAdditionRequest(BaseModel):
    rating: int
    review_text: str
    tutor_mail: str
    student_mail: str


class CourseAdditionRequest(BaseModel):
    tutor_mail: str
    course_name: str
    course_price: int


class CourseDeletionRequest(BaseModel):
    tutor_mail: str
    course_name: str


class HomeworkAdditionRequest(BaseModel):
    tutor_mail: str
    student_mail: str
    homework: str


class MessageToStudentRequest(BaseModel):
    message_text: str
    tutor_mail: str
    student_mail: str


@tutor_api.get("/tutor/{tutor_mail}")
async def get_tutor_profile(
    tutor_mail: str, core: OlympianTutorService = Depends(get_core)
):
    return core.tutor_interactor.get_tutor(tutor_mail)


@tutor_api.get("/tutor/courses/{tutor_mail}")
async def get_tutor_courses(
    tutor_mail: str, core: OlympianTutorService = Depends(get_core)
):
    tutor_courses = core.course_interactor.get_tutor_courses(tutor_mail)
    print(tutor_courses)
    return tutor_courses


@tutor_api.get("/tutor/reviews/{tutor_mail}")
async def get_tutor_reviews(
    tutor_mail: str, core: OlympianTutorService = Depends(get_core)
):
    tutor_reviews = core.review_interactor.get_tutor_reviews(tutor_mail)
    return tutor_reviews


@tutor_api.get("/tutor/lessons/{tutor_mail}")
async def get_tutor_lessons(
    tutor_mail: str, core: OlympianTutorService = Depends(get_core)
):
    tutor_lessons = core.lesson_interactor.get_tutor_lessons(tutor_mail)
    return tutor_lessons


@tutor_api.get("/tutor/students/{tutor_mail}")
async def get_tutor_students(
    tutor_mail: str, core: OlympianTutorService = Depends(get_core)
):
    tutor_students: List[Student] = []
    tutor_mails: set[str] = set()
    tutor_lesson_students = core.lesson_interactor.get_tutor_students(tutor_mail)
    for tutor_student_mail in tutor_lesson_students:
        if tutor_student_mail not in tutor_mails:
            student = core.student_interactor.get_student(tutor_student_mail)
            tutor_students.append(student)
            tutor_mails.add(tutor_student_mail)
    print(tutor_students)
    return tutor_students


@tutor_api.get("/tutor/messaged_students/{tutor_mail}")
async def get_student_messaged_tutors(
    tutor_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    print("/tutor/" + tutor_mail)

    tutor_messaged_students = core.message_interactor.get_tutor_messaged_students(
        tutor_mail
    )
    print(tutor_messaged_students)
    return tutor_messaged_students


@tutor_api.get("/tutor/messages/{tutor_mail}/{student_mail}")
async def get_tutor_messages(
    tutor_mail: str,
    student_mail: str,
    core: OlympianTutorService = Depends(get_core),
):
    print("/student/lessons/" + student_mail)

    messages = core.message_interactor.get_messages(tutor_mail, student_mail)
    print(messages)
    return messages


@tutor_api.post("/tutor/add_review")
async def add_review(
    review_addition: ReviewAdditionRequest,
    core: OlympianTutorService = Depends(get_core),
):
    print(review_addition.rating)
    review_score = review_addition.rating
    review_text = review_addition.review_text
    tutor_mail = review_addition.tutor_mail
    student_mail = review_addition.student_mail
    core.review_interactor.create_review(review_text, tutor_mail, student_mail)
    core.tutor_ranking_interactor.add_review_score(tutor_mail, review_score)
    return review_addition


@tutor_api.post("/tutor/message_to_student")
async def message_to_student(
    data: MessageToStudentRequest,
    core: OlympianTutorService = Depends(get_core),
):
    message_text = data.message_text
    tutor_mail = data.tutor_mail
    student_mail = data.student_mail
    student = core.student_interactor.get_student(student_mail)
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if student is None:
        return {"message": "Student with this visitor mail doesn't exits"}
    if tutor is None:
        return {"message": "Tutor with this mail doesn't exist."}
    print(data)
    core.message_interactor.create_message(message_text, tutor_mail, student_mail)
    return {"message": "Message sent successfully."}


@tutor_api.post("/tutor/add_homework")
async def add_homework(
    homework_addition: HomeworkAdditionRequest,
    core: OlympianTutorService = Depends(get_core),
):
    tutor_mail = homework_addition.tutor_mail
    student_mail = homework_addition.student_mail
    homework = homework_addition.homework
    print(homework_addition)
    core.homework_interactor.create_homework(homework, tutor_mail, student_mail)


@tutor_api.post("/tutor/change_bio")
def tutor_change_bio(
    change_bio: ChangeBioRequest, core: OlympianTutorService = Depends(get_core)
):
    tutor_mail = change_bio.tutor_mail
    new_bio = change_bio.new_bio
    print(change_bio)
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if tutor is None:
        return {"message": "No such tutor exists."}
    core.tutor_interactor.change_tutor_biography(tutor_mail, new_bio)
    return {"message": "Bio changed successfully!"}


@tutor_api.post("/withdrawal_request")
def tutor_withdrawal_request(
    withdrawal_request: MoneyWithdrawalRequest,
    core: OlympianTutorService = Depends(get_core),
):
    tutor_mail = withdrawal_request.tutor_mail
    amount = withdrawal_request.amount
    print(withdrawal_request)
    tutor = core.tutor_interactor.get_tutor(tutor_mail)
    if tutor is None:
        return {"message": "No such tutor exists."}
    tutor_balance = core.tutor_interactor.get_tutor_balance(tutor_mail)
    if amount > tutor_balance:
        return {"message": "Not enough money on your balance"}
    core.tutor_interactor.decrease_tutor_balance(tutor_mail, amount)
    return {"message": "Money withdrawal successfully!"}


@tutor_api.post("/tutor/upload_profile_picture/{tutor_mail}")
async def create_upload_file(
    tutor_mail: str,
    file: UploadFile = File(...),
    core: OlympianTutorService = Depends(get_core),
):
    dest_path = "../../frontend/src/Storage/" + tutor_mail
    async with aiofiles.open(dest_path, "wb") as dest_file:
        content = await file.read()
        await dest_file.write(content)

    core.tutor_interactor.change_tutor_profile_address(tutor_mail, dest_path)


@tutor_api.post("/tutor/add_course")
async def add_course(
    course_addition: CourseAdditionRequest,
    core: OlympianTutorService = Depends(get_core),
):
    print(course_addition)
    tutor_mail = course_addition.tutor_mail
    course_name = course_addition.course_name
    course_price = course_addition.course_price
    if course_price <= 0:
        return {"message": "Course price can not be negative!"}
    tutor = core.tutor_interactor.get_tutor(tutor_mail)

    if tutor is None:
        return {"message": "No such tutor exists!"}

    core.course_interactor.create_course(course_name, tutor_mail, course_price)
    core.tutor_ranking_interactor.set_minimum_lesson_price(tutor_mail, course_price)
    return {"message": "Course added successfully."}


@tutor_api.delete("/tutor/delete_course")
def delete_course(
    course_deletion: CourseDeletionRequest,
    core: OlympianTutorService = Depends(get_core),
):
    print(course_deletion)
    course_name = course_deletion.course_name
    tutor_mail = course_deletion.tutor_mail
    core.course_interactor.delete_course(tutor_mail, course_name)
