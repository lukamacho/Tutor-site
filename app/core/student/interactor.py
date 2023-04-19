from dataclasses import dataclass
from typing import Protocol

from app.core.student.entity import Student


class IStudentInteractor(Protocol):
    def create_student(self, email: str, password: str) -> Student:
        return None


@dataclass
class StudentInteractor:
    def create_student(self, email: str, password: str) -> Student:
        return None
