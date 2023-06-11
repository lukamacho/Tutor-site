from dataclasses import dataclass
from typing import Optional, Protocol

from app.core.lesson.entity import Lesson


class ILessonRepository(Protocol):
    def create_lesson(
        self,
        subject: str,
        tutor_mail: str,
        student_mail: str,
        number_of_lessons: int,
        lesson_price: int,
    ) -> Lesson:
        pass

    def get_lesson(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> Optional[Lesson]:
        pass

    def get_number_of_lessons(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> int:
        pass

    def set_number_of_lessons(
        self, tutor_mail: str, student_mail: str, new_number: int, subject: str
    ) -> None:
        pass

    def decrease_lesson_number(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> None:
        pass

    def increase_lesson_number(
        self, tutor_mail: str, student_mail: str, added_lessons: int, subject: str
    ) -> None:
        pass

    def set_lesson_price(
        self, tutor_mail: str, student_mail: str, subject: str, new_price: int
    ) -> None:
        pass


class ILessonInteractor(Protocol):
    def create_lesson(
        self,
        subject: str,
        tutor_mail: str,
        student_mail: str,
        number_of_lessons: int,
        lesson_price: int,
    ) -> Lesson:
        pass

    def get_lesson(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> Optional[Lesson]:
        pass

    def get_number_of_lessons(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> int:
        pass

    def set_number_of_lessons(
        self, tutor_mail: str, student_mail: str, new_number: int, subject: str
    ) -> None:
        pass

    def decrease_lesson_number(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> None:
        pass

    def increase_lesson_number(
        self, tutor_mail: str, student_mail: str, added_lessons: int, subject: str
    ) -> None:
        pass

    def set_lesson_price(
        self, tutor_mail: str, student_mail: str, subject: str, new_price: int
    ) -> None:
        pass


@dataclass
class LessonInteractor:
    lesson_interactor: ILessonRepository

    def create_lesson(
        self,
        subject: str,
        tutor_mail: str,
        student_mail: str,
        number_of_lessons: int,
        lesson_price: int,
    ) -> Lesson:
        return self.lesson_interactor.create_lesson(
            subject, tutor_mail, student_mail, number_of_lessons, lesson_price
        )

    def get_lesson(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> Optional[Lesson]:
        return self.lesson_interactor.get_lesson(tutor_mail, student_mail, subject)

    def get_number_of_lessons(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> int:
        return self.lesson_interactor.get_number_of_lessons(
            tutor_mail, student_mail, subject
        )

    def set_number_of_lessons(
        self, tutor_mail: str, student_mail: str, new_number: int, subject: str
    ) -> None:
        self.lesson_interactor.set_number_of_lessons(
            tutor_mail, student_mail, new_number, subject
        )

    def decrease_lesson_number(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> None:
        self.lesson_interactor.decrease_lesson_number(tutor_mail, student_mail, subject)

    def increase_lesson_number(
        self, tutor_mail: str, student_mail: str, added_lessons: int, subject: str
    ) -> None:
        self.lesson_interactor.increase_lesson_number(
            tutor_mail, student_mail, added_lessons, subject
        )

    def set_lesson_price(
        self, tutor_mail: str, student_mail: str, subject: str, new_price: int
    ) -> None:
        self.lesson_interactor.set_lesson_price(
            tutor_mail, student_mail, subject, new_price
        )
