from dataclasses import dataclass, field
from typing import List

from app.core.lesson.entity import Lesson


@dataclass
class InMemoryLessonRepository:
    data: List[Lesson] = field(default_factory=list)

    def create_lesson(
        self,
        subject: str,
        tutor_mail: str,
        student_mail: str,
        number_of_lessons: int,
        lesson_price: int,
    ) -> Lesson:
        lesson = Lesson(
            subject, tutor_mail, student_mail, number_of_lessons, lesson_price
        )
        self.data.append(lesson)
        return lesson

    def get_lesson(self, tutor_mail: str, student_mail: str, subject: str) -> Lesson:
        for lesson in self.data:
            if (
                lesson.subject == subject
                and lesson.tutor_mail == tutor_mail
                and lesson.student_mail == student_mail
            ):
                return lesson
        return Lesson("", "", "", 0, 0)

    def get_number_of_lessons(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> int:
        for lesson in self.data:
            if (
                lesson.subject == subject
                and lesson.tutor_mail == tutor_mail
                and lesson.student_mail == student_mail
            ):
                return lesson.number_of_lessons
        return 0

    def set_number_of_lessons(
        self, tutor_mail: str, student_mail: str, new_number: int, subject: str
    ) -> None:
        for lesson in self.data:
            if (
                lesson.subject == subject
                and lesson.tutor_mail == tutor_mail
                and lesson.student_mail == student_mail
            ):
                lesson.number_of_lessons = new_number

    def decrease_lesson_number(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> None:
        for lesson in self.data:
            if (
                lesson.subject == subject
                and lesson.tutor_mail == tutor_mail
                and lesson.student_mail == student_mail
            ):
                lesson.number_of_lessons -= 1

    def increase_lesson_number(
        self, tutor_mail: str, student_mail: str, added_lessons: int, subject: str
    ) -> None:
        for lesson in self.data:
            if (
                lesson.subject == subject
                and lesson.tutor_mail == tutor_mail
                and lesson.student_mail == student_mail
            ):
                lesson.number_of_lessons += added_lessons

    def set_lesson_price(
        self, tutor_mail: str, student_mail: str, subject: str, new_price: int
    ) -> None:
        for lesson in self.data:
            if (
                lesson.subject == subject
                and lesson.tutor_mail == tutor_mail
                and lesson.student_mail == student_mail
            ):
                lesson.lesson_price = new_price
