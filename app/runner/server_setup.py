from typing import Protocol

from fastapi import FastAPI

from app.core.facade import OlympianTutorService
from app.infra.emailer.smtp import SMTPEmailService
from app.infra.fastapi.api_main import setup_fastapi
from app.infra.sqlite.course import SqlCourseRepository
from app.infra.sqlite.lesson import SqlLessonRepository
from app.infra.sqlite.message import SqlMessageRepository
from app.infra.sqlite.review import SqlReviewRepository
from app.infra.sqlite.student import SqlStudentRepository
from app.infra.sqlite.tutors import SqlTutorRepository


def setup_student_repository() -> SqlStudentRepository:
    return SqlStudentRepository("db.db")


def setup_tutor_repository() -> SqlTutorRepository:
    return SqlTutorRepository("db.db")


def setup_message_repository() -> SqlMessageRepository:
    pass


def setup_course_repository() -> SqlCourseRepository:
    return SqlCourseRepository("db.db")


def setup_review_repository() -> SqlReviewRepository:
    return SqlReviewRepository("db.db")


def setup_lesson_repository() -> SqlLessonRepository:
    return SqlLessonRepository("db.db")


def setup() -> FastAPI:
    student_repository = setup_student_repository()
    tutor_repository = setup_tutor_repository()
    course_repository = setup_course_repository()
    lesson_repository = setup_lesson_repository()
    review_repository = setup_review_repository()


    return setup_fastapi(
        OlympianTutorService.create(
            emailer=SMTPEmailService,
            course_interactor=course_repository,
            review_interactor=review_repository,
            lesson_interactor=lesson_repository,
            student_interactor=student_repository,
            tutor_interactor=tutor_repository,
        )
    )
