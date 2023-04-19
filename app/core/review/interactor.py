from dataclasses import dataclass
from typing import Protocol, Optional, List

from app.core.review.entity import Review


class IReviewRepository(Protocol):
    def create_course(self, subject: str, tutor_mail: str, price: int) -> Review:
        pass

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Review]:
        pass

    def get_courses(self, tutor_mail: str) -> Optional[List[Review]]:
        pass


class ICourseInteractor(Protocol):
    def create_course(self, subject: str, tutor_mail: str, price: int) -> Review:
        pass

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Review]:
        pass

    def get_courses(self, tutor_mail: str) -> Optional[List[Review]]:
        pass


@dataclass
class ReviewInteractor:
    course_repository: IReviewRepository

    def get_course(
        self,
    ) -> None:
        self.course_repository.get_course()

    def create_course(self):
        self.course_repository.create_course()

    def get_courses(self):
        self.course_repository.get_courses()
