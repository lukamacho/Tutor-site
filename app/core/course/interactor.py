from dataclasses import dataclass
from typing import List, Optional, Protocol

from app.core.course.entity import Course


class ICourseRepository(Protocol):
    def create_course(self, subject: str, tutor_mail: str, price: int) -> Course:
        pass

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Course]:
        pass

    def get_tutor_courses(self, tutor_mail: str) -> Optional[List[Course]]:
        pass

    def get_courses(self) -> Optional[List[Course]]:
        pass


class ICourseInteractor(Protocol):
    def create_course(self, subject: str, tutor_mail: str, price: int) -> Course:
        pass

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Course]:
        pass

    def get_tutor_courses(self, tutor_mail: str) -> Optional[List[Course]]:
        pass

    def get_courses(self) -> Optional[List[Course]]:
        pass


@dataclass
class CourseInteractor:
    course_repository: ICourseRepository

    def create_course(self, subject: str, tutor_mail: str, price: int) -> Course:
        return self.course_repository.create_course(subject, tutor_mail, price)

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Course]:
        return self.course_repository.get_course(subject, tutor_mail)

    def get_tutor_courses(self, tutor_mail: str) -> Optional[List[Course]]:
        return self.course_repository.get_tutor_courses(tutor_mail)

    def get_courses(self) -> Optional[List[Course]]:
        return self.course_repository.get_courses()
