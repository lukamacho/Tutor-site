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

    def delete_course(self, tutor_mail: str, subject: str) -> None:
        pass

    def change_price(self, tutor_mail: str, subject: str, course_price: int) -> None:
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

    def delete_course(self, tutor_mail: str, subject: str) -> None:
        pass

    def change_price(self, tutor_mail: str, subject: str, course_price: int) -> None:
        pass


@dataclass
class CourseInteractor:
    course_repository: ICourseRepository

    def create_course(self, subject: str, tutor_mail: str, price: int) -> Course:
        return self.course_repository.create_course(subject, tutor_mail, price)

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Course]:
        return self.course_repository.get_course(subject, tutor_mail)

    def get_courses(self, tutor_mail: str) -> Optional[List[Course]]:
        return self.course_repository.get_courses(tutor_mail)

    def delete_course(self, tutor_mail: str, subject: str) -> None:
        return self.course_repository.delete_course(tutor_mail, subject)

    def change_price(self, tutor_mail: str, subject: str, course_price: int) -> None:
        return self.course_repository.change_price(tutor_mail, subject, course_price)
    def get_tutor_courses(self, tutor_mail: str) -> Optional[List[Course]]:
        return self.course_repository.get_tutor_courses(tutor_mail)

    def get_courses(self) -> Optional[List[Course]]:
        return self.course_repository.get_courses()