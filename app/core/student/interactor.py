from dataclasses import dataclass

from app.core.student.entity import Student


@dataclass
class StudentInteractor:
    def create_student(self, email: str, password: str) -> Student:
        return None
