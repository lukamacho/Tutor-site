from dataclasses import dataclass
from typing import Protocol, Optional

from app.core.student.entity import Student


class IStudentInteractor(Protocol):
    def create_student(
        self, first_name: str, last_name: str, email: str, password: str, balance: int
    ) -> Student:
        pass

    def get_student(self, email: str) -> Optional[Student]:
        pass

    def set_balance(self, student_mail: str, new_balance: int) -> None:
        pass

    def get_balance(self, student_mail: str) -> int:
        pass

    def increase_balance(self, student_mail: str, amount: int) -> None:
        pass

    def decrease_balance(self, student_mail: str, amount: int) -> None:
        pass

    def change_first_name(self, student_mail: str, first_name: str) -> None:
        pass

    def change_last_name(self, student_mail: str, last_name: str) -> None:
        pass


class IStudentRepository(Protocol):
    def create_student(
        self, first_name: str, last_name: str, email: str, password: str, balance: int
    ) -> Student:
        pass

    def get_student(self, email: str) -> Optional[Student]:
        pass

    def set_balance(self, student_mail: str, new_balance: int) -> None:
        pass

    def get_balance(self, student_mail: str) -> int:
        pass

    def increase_balance(self, student_mail: str, amount: int) -> None:
        pass

    def decrease_balance(self, student_mail: str, amount: int) -> None:
        pass

    def change_first_name(self, student_mail: str, first_name: str) -> None:
        pass

    def change_last_name(self, student_mail: str, last_name: str) -> None:
        pass


@dataclass
class StudentInteractor:
    student_repository: IStudentRepository

    def create_student(self, email: str, password: str) -> Student:
        return self.student_repository.create_student(email, password)

    def get_student(self, email: str) -> Optional[Student]:
        return self.student_repository.get_student(email)

    def set_balance(self, student_mail: str, new_balance: int) -> None:
        self.student_repository.set_balance(student_mail, new_balance)

    def get_balance(self, student_mail: str) -> int:
        return self.student_repository.get_balance(student_mail)

    def increase_balance(self, student_mail: str, amount: int) -> None:
        self.student_repository.increase_balance(student_mail, amount)

    def decrease_balance(self, student_mail: str, amount: int) -> None:
        self.student_repository.decrease_balance(student_mail, amount)

    def change_first_name(self, student_mail: str, first_name: str) -> None:
        self.student_repository.change_first_name(student_mail, first_name)

    def change_last_name(self, student_mail: str, last_name: str) -> None:
        self.student_repository.change_last_name(student_mail, last_name)
