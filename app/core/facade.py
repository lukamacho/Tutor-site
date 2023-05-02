from dataclasses import dataclass
from typing import Optional, List

from app.core.admin.interactor import AdminInteractor, IEmailService
from app.core.course.interactor import CourseInteractor, ICourseInteractor
from app.core.lesson.entity import Lesson
from app.core.lesson.interactor import LessonInteractor, ILessonInteractor
from app.core.review.entity import Review
from app.core.review.interactor import ReviewInteractor, IReviewInteractor
from app.core.student.entity import Student
from app.core.student.interactor import IStudentInteractor, StudentInteractor
from app.core.tutor.entity import Tutor
from app.core.tutor.interactor import TutorInteractor, ITutorInteractor


@dataclass
class OlympianTutorService:
    admin_interactor: AdminInteractor
    course_interactor: CourseInteractor
    review_interactor: ReviewInteractor
    lesson_interactor: LessonInteractor
    student_interactor: StudentInteractor
    tutor_interactor: TutorInteractor

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

    def create_student(
        self, first_name: str, last_name: str, email: str, password: str, balance: int
    ) -> Student:
        return self.student_repository.create_student(
            first_name, last_name, email, password, balance
        )

    def get_student(self, email: str) -> Optional[Student]:
        return self.student_repository.get_student(email)

    def set_student_balance(self, student_mail: str, new_balance: int) -> None:
        self.student_repository.set_balance(student_mail, new_balance)

    def get_student_balance(self, student_mail: str) -> int:
        return self.student_repository.get_balance(student_mail)

    def increase_student_balance(self, student_mail: str, amount: int) -> None:
        self.student_repository.increase_balance(student_mail, amount)

    def decrease_student_balance(self, student_mail: str, amount: int) -> None:
        self.student_repository.decrease_balance(student_mail, amount)

    def change_student_first_name(self, student_mail: str, first_name: str) -> None:
        self.student_repository.change_first_name(student_mail, first_name)

    def change_student_last_name(self, student_mail: str, last_name: str) -> None:
        self.student_repository.change_last_name(student_mail, last_name)

    def create_tutor(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        balance: int,
        biography: str,
    ) -> Tutor:
        return self.tutor_repository.create_tutor(
            first_name, last_name, email, password, balance, biography
        )

    def get_tutor(self, email: str) -> Optional[Tutor]:
        return self.tutor_repository.get_tutor(email)

    def set_tutor_balance(self, tutor_mail: str, new_balance: int) -> None:
        self.tutor_repository.set_balance(tutor_mail, new_balance)

    def get_tutor_balance(self, tutor_mail: str) -> int:
        return self.tutor_repository.get_balance(tutor_mail)

    def increase_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        self.tutor_repository.increase_balance(tutor_mail, amount)

    def decrease_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        self.tutor_repository.decrease_balance(tutor_mail, amount)

    def set_commission_pct(self, tutor_mail: str, new_commission_pct: float):
        self.tutor_repository.set_commission_pct(tutor_mail, new_commission_pct)

    def decrease_commission_pct(self, tutor_mail: str) -> None:
        self.tutor_repository.decrease_balance(tutor_mail)

    def change_tutor_first_name(self, tutor_mail: str, first_name: str) -> None:
        self.tutor_repository.change_first_name(tutor_mail, first_name)

    def change_tutor_last_name(self, tutor_mail: str, last_name: str) -> None:
        self.tutor_repository.change_last_name(tutor_mail, last_name)

    def change_tutor_biography(self, tutor_mail: str, biography: str) -> None:
        self.tutor_repository.change_biography(tutor_mail, biography)

    @classmethod
    def create(
        cls,
        emailer: IEmailService,
        course_interactor: ICourseInteractor,
        review_interactor: IReviewInteractor,
        lesson_interactor: ILessonInteractor,
        student_interactor: IStudentInteractor,
        tutor_interactor: ITutorInteractor,
    ) -> "OlympianTutorService":
        return cls(
            admin_interactor=AdminInteractor(emailer),
            course_interactor=CourseInteractor(course_interactor),
            review_interactor=ReviewInteractor(review_interactor),
            lesson_interactor=LessonInteractor(lesson_interactor),
            student_interactor=StudentInteractor(student_interactor),
            tutor_interactor=TutorInteractor(tutor_interactor),
        )
