from dataclasses import dataclass, field
from typing import List

from app.core.course.entity import Course


@dataclass
class InMemoryCourseRepository:
    data: List[Course] = field(default_factory=list)

    def create_course(self, subject: str, tutor_mail: str, price: int) -> Course:
        course = Course(subject, tutor_mail, price)
        self.data.append(course)
        return course

    def get_course(self, subject: str, tutor_mail: str) -> Course:
        for course in self.data:
            if course.subject == subject and course.tutor_mail == tutor_mail:
                return course
        return Course("", "", 0)

    def get_tutor_courses(self, tutor_mail: str) -> List[Course]:
        courses: List[Course] = []
        for course in self.data:
            if course.tutor_mail == tutor_mail:
                courses.append(course)
        return courses

    def get_courses(self) -> List[Course]:
        return self.data

    def delete_course(self, tutor_mail: str, subject: str) -> None:
        course = self.get_course(subject, tutor_mail)
        self.data.remove(course)
