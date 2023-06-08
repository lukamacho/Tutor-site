from dataclasses import dataclass
from typing import Optional, Protocol

from app.core.student.entity import Student


class IStudentInteractor(Protocol):
    def create_student(
        self, first_name: str, last_name: str, email: str, password: str, balance: int
    ) -> Student:
        pass

    def get_student(self, email: str) -> Optional[Student]:
        pass

    def set_student_balance(self, student_mail: str, new_balance: int) -> None:
        pass

    def get_student_balance(self, student_mail: str) -> int:
        pass

    def increase_student_balance(self, student_mail: str, amount: int) -> None:
        pass

    def decrease_student_balance(self, student_mail: str, amount: int) -> None:
        pass

    def change_student_first_name(self, student_mail: str, first_name: str) -> None:
        pass

    def change_student_last_name(self, student_mail: str, last_name: str) -> None:
        pass

    def change_student_password(self, student_mail: str, password: str) -> None:
        pass

    def change_student_profile_address(self, student_mail: str, profile_address: str) -> None:
        pass


class IStudentRepository(Protocol):
    def create_student(
        self, first_name: str, last_name: str, email: str, password: str, balance: int
    ) -> Student:
        pass

    def get_student(self, email: str) -> Optional[Student]:
        pass

    def set_student_balance(self, student_mail: str, new_balance: int) -> None:
        pass

    def get_student_balance(self, student_mail: str) -> int:
        pass

    def increase_student_balance(self, student_mail: str, amount: int) -> None:
        pass

    def decrease_student_balance(self, student_mail: str, amount: int) -> None:
        pass

    def change_student_first_name(self, student_mail: str, first_name: str) -> None:
        pass

    def change_student_last_name(self, student_mail: str, last_name: str) -> None:
        pass

    def delete_student(self, student_mail: str) -> None:
        pass

    def change_student_password(self, student_mail: str, password: str) -> None:
        pass

    def change_student_profile_address(self, student_mail: str, profile_address: str) -> None:
        pass


@dataclass
class StudentInteractor:
    student_repository: IStudentRepository

    def create_student(
        self, first_name: str, last_name: str, email: str, password: str, balance: int
    ) -> Student:
        return self.student_repository.create_student(
            first_name, last_name, email, password, balance
        )

    def get_student(self, email: str) -> Optional[Student]:
        return self.student_repository.get_student(email)

    def set_student_balance(self, student_mail: str, new_balance: int) -> None:
        self.student_repository.set_student_balance(student_mail, new_balance)

    def get_student_balance(self, student_mail: str) -> int:
        return self.student_repository.get_student_balance(student_mail)

    def increase_student_balance(self, student_mail: str, amount: int) -> None:
        self.student_repository.increase_student_balance(student_mail, amount)

    def decrease_student_balance(self, student_mail: str, amount: int) -> None:
        self.student_repository.decrease_student_balance(student_mail, amount)

    def change_student_first_name(self, student_mail: str, first_name: str) -> None:
        self.student_repository.change_student_first_name(student_mail, first_name)

    def change_student_last_name(self, student_mail: str, last_name: str) -> None:
        self.student_repository.change_student_last_name(student_mail, last_name)

    def change_student_profile_address(self, student_mail: str, profile_address: str) -> None:
        self.student_repository.change_student_profile_address(student_mail, profile_address)

    def delete_student(self, student_mail: str) -> None:
        self.student_repository.delete_student(student_mail)

    def change_student_password(self, student_mail: str, password: str) -> None:
        self.student_repository.change_student_password(student_mail, password)
