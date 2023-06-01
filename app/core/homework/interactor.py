from dataclasses import dataclass
from typing import List, Protocol

from app.core.homework.entity import Homework


class IHomeworkInteractor(Protocol):
    def create_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> Homework:
        pass

    def change_homework(
        self,
        new_homework_text: str,
        old_homework_text: str,
        tutor_mail: str,
        student_mail: str,
    ) -> Homework:
        pass

    def get_student_homework(self, student_mail: str) -> List[Homework]:
        pass

    def delete_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        pass


class IHomeworkRepository(Protocol):
    def create_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> Homework:
        pass

    def change_homework(
        self,
        new_homework_text: str,
        old_homework_text: str,
        tutor_mail: str,
        student_mail: str,
    ) -> Homework:
        pass

    def get_student_homework(self, student_mail: str) -> List[Homework]:
        pass

    def delete_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        pass


@dataclass
class HomeworkInteractor:
    homework_repository: IHomeworkRepository

    def create_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> Homework:
        return self.homework_repository.create_homework(
            homework_text, tutor_mail, student_mail
        )

    def change_homework(
        self,
        new_homework_text: str,
        old_homework_text: str,
        tutor_mail: str,
        student_mail: str,
    ) -> Homework:
        return self.homework_repository.change_homework(
            new_homework_text, old_homework_text, tutor_mail, student_mail
        )

    def get_student_homework(self, student_mail: str) -> List[Homework]:
        return self.homework_repository.get_student_homework(student_mail)

    def delete_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        self.homework_repository.delete_homework(
            homework_text, tutor_mail, student_mail
        )
