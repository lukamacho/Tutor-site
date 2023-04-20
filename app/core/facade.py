from dataclasses import dataclass
from typing import Optional, List

from app.core.admin.interactor import AdminInteractor, IEmailService
from app.core.course.interactor import CourseInteractor, ICourseInteractor
from app.core.lesson.interactor import LessonInteractor, ILessonInteractor
from app.core.review.entity import Review
from app.core.review.interactor import ReviewInteractor, IReviewInteractor


@dataclass
class OlympianTutorService:
    admin_interactor: AdminInteractor
    course_interactor: CourseInteractor
    review_interactor: ReviewInteractor
    lesson_interactor: LessonInteractor

    def send_hello(self):
        self.admin_interactor.send_hello()

    def send_verification(self):
        self.admin_interactor.verify_mail()

    def get_course(self):
        self.course_interactor.get_course()

    def create_review(
        self, review_text: str, tutor_mail: str, student_mail: str
    ) -> Review:
        return self.review_repository.create_review(
            review_text, tutor_mail, student_mail
        )

    def get_review(self, tutor_mail: str, student_mail: str) -> Optional[Review]:
        return self.review_repository.get_review(tutor_mail, student_mail)

    def get_tutor_reviews(self, tutor_mail: str) -> List[Review]:
        return self.review_repository.get_review(tutor_mail)

    def delete_review(self, tutor_mail: str, student_mail: str) -> None:
        self.review_repository.delete_review(tutor_mail, student_mail)

    def change_review(
        self, new_review_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        self.review_repository.change_review(new_review_text, tutor_mail, student_mail)

    def create_lesson(
        self,
        subject: str,
        tutor_mail: str,
        student_mail: str,
        number_of_lessons: int,
        lesson_price: int,
    ) -> Lesson:
        return self.lesson_interactor.get_lesson(
            subject, tutor_mail, student_mail, number_of_lessons, lesson_price
        )

    def get_lesson(self, tutor_mail: str, student_mail: str, subject: str) -> Lesson:
        return self.lesson_interactor.get_lesson(tutor_mail, student_mail, subject)

    def get_number_of_lessons(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> int:
        return self.lesson_interactor.get_number_of_lessons(
            tutor_mail, student_mail, subject
        )

    def set_number_of_lessons(
        self, tutor_mail: str, student_mail: str, new_number: int, subject: str
    ) -> None:
        self.lesson_interactor.set_number_of_lessons(
            tutor_mail, student_mail, new_number, subject
        )

    def decrease_lesson_number(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> None:
        self.lesson_interactor.decrease_lesson_number(tutor_mail, student_mail, subject)

    def increase_lesson_number(
        self, tutor_mail: str, student_mail: str, added_lessons: int, subject: str
    ) -> None:
        self.lesson_interactor.increase_lesson_number(
            tutor_mail, student_mail, added_lessons, subject
        )

    def set_lesson_price(
        self, tutor_mail: str, student_mail: str, subject: str, new_price: int
    ) -> None:
        self.lesson_interactor.set_lesson_price(
            tutor_mail, student_mail, subject, new_price
        )

    @classmethod
    def create(
        cls,
        emailer: IEmailService,
        course_interactor: ICourseInteractor,
        review_interactor: IReviewInteractor,
        lesson_interactor: ILessonInteractor,
    ) -> "OlympianTutorService":
        return cls(
            admin_interactor=AdminInteractor(emailer),
            course_interactor=CourseInteractor(course_interactor),
            review_interactor=ReviewInteractor(review_interactor),
            lesson_interactor=LessonInteractor(lesson_interactor),
        )
