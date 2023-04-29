from dataclasses import dataclass, field
from typing import Dict, Optional
from app.core.student.entity import Student


@dataclass
class InMemoryStudentRepository:
    data: Dict[str, Student] = field(default_factory=dict)

    def create_student(
            self, first_name: str, last_name: str, email: str, password: str, balance: int
    ) -> Student:
        student = Student(first_name, last_name, email, password, balance)
        self.data[email] = student
        return student

    def get_student(self, email: str) -> Optional[Student]:
        if email in self.data.keys():
            return self.data[email]
        return None

    def set_balance(self, student_mail: str, new_balance: int) -> None:
        student = self.get_student(student_mail)
        if student is not None:
            student.set_balance(new_balance)

    def get_balance(self, student_mail: str) -> Optional[int]:
        student = self.get_student(student_mail)
        if student is not None:
            return student.get_balance()
        return None

    def increase_balance(self, student_mail: str, amount: int) -> None:
        student = self.get_student(student_mail)
        if student is not None:
            return student.increase_balance(amount)

    def decrease_balance(self, student_mail: str, amount: int) -> None:
        student = self.get_student(student_mail)
        if student is not None:
            return student.decrease_balance(amount)

    def change_first_name(self, student_mail: str, first_name: str) -> None:
        student = self.get_student(student_mail)
        if student is not None:
            student.change_first_name(first_name)

    def change_last_name(self, student_mail: str, last_name: str) -> None:
        student = self.get_student(student_mail)
        if student is not None:
            student.change_last_name(last_name)
