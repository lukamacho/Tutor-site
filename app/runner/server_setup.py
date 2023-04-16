from typing import Protocol

from fastapi import FastAPI

from app.infra.fastapi.api_main import setup_fastapi
from app.infra.sqlite.course import SqlCourseRepository
from app.infra.sqlite.lesson import SqlLessonRepository
from app.infra.sqlite.students import SqlStudentRepository
from app.infra.sqlite.tutors import SqlTutorRepository


def setup_student_repository() -> SqlStudentRepository:
    return SqlStudentRepository("db.db")


def setup_tutor_repository() -> SqlTutorRepository:
    return SqlTutorRepository("db.db")


def setup_course_repository() -> SqlCourseRepository:
    return SqlCourseRepository("db.db")


def setup_lesson_repository() -> SqlLessonRepository:
    return SqlLessonRepository("db.db")


def setup() -> FastAPI:
    student_repository = setup_student_repository()
    tutor_repository = setup_tutor_repository()
    course_repository = setup_course_repository()
    lesson_repository = setup_lesson_repository()

    return setup_fastapi()
