from dataclasses import dataclass
from typing import Protocol, Optional, List

from app.core.course.entity import Course


class ICourseRepository(Protocol):
    def create_course(self, subject: str, tutor_mail: str, price: int) -> Course:
        pass

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Course]:
        pass

    def get_courses(self, tutor_mail: str) -> Optional[List[Course]]:
        pass


class ICourseInteractor(Protocol):
    def create_course(self, subject: str, tutor_mail: str, price: int) -> Course:
        pass

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Course]:
        pass

    def get_courses(self, tutor_mail: str) -> Optional[List[Course]]:
        pass


@dataclass
class CourseInteractor:
    course_repository: ICourseRepository

    def get_course(
        self,
    ) -> None:
        self.course_repository.get_course()

    def create_course(self):
        self.course_repository.create_course()

    def get_courses(self):
        self.course_repository.get_courses()
