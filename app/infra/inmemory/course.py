from dataclasses import dataclass, field
from typing import List, Optional

from app.core.course.entity import Course


@dataclass
class InMemoryCourseRepository:
    data: List[Course] = field(default_factory=list)

    def create_course(self, subject: str, tutor_mail: str, price: int) -> Course:
        course = Course(subject, tutor_mail, price)
        self.data.append(course)
        return course

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Course]:
        for course in self.data:
            if course.subject == subject and course.tutor_mail == tutor_mail:
                return course
        return None

    def get_courses(self, tutor_mail: str) -> Optional[List[Course]]:
        courses: List[Course] = []
        for course in self.data:
            if course.tutor_mail == tutor_mail:
                courses.append(course)
        return courses
