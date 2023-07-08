from dataclasses import dataclass
from typing import List

from app.core.course.entity import Course
from app.core.course.interactor import CourseInteractor, ICourseInteractor
from app.core.homework.entity import Homework
from app.core.homework.interactor import HomeworkInteractor, IHomeworkInteractor
from app.core.lesson.entity import Lesson
from app.core.lesson.interactor import ILessonInteractor, LessonInteractor
from app.core.message.entity import Message
from app.core.message.interactor import IMessageInteractor, MessageInteractor
from app.core.review.entity import Review
from app.core.review.interactor import IReviewInteractor, ReviewInteractor
from app.core.student.entity import Student
from app.core.student.interactor import IStudentInteractor, StudentInteractor
from app.core.tutor.entity import Tutor
from app.core.tutor.interactor import ITutorInteractor, TutorInteractor
from app.core.tutor_ranking.interactor import (
    ITutorRankingInteractor,
    TutorRankingInteractor,
)


@dataclass
class OlympianTutorService:
    course_interactor: CourseInteractor
    review_interactor: ReviewInteractor
    lesson_interactor: LessonInteractor
    student_interactor: StudentInteractor
    tutor_interactor: TutorInteractor
    homework_interactor: HomeworkInteractor
    message_interactor: MessageInteractor
    tutor_ranking_interactor: TutorRankingInteractor

    def add_tutor_in_ranking(
        self,
        email: str,
    ) -> None:
        self.tutor_ranking_interactor.add_tutor_in_ranking(email)

    def get_review_scores(self, email: str) -> int:
        return self.tutor_ranking_interactor.get_review_scores(email)

    def get_number_of_reviews(self, email: str) -> int:
        return self.tutor_ranking_interactor.get_number_of_reviews(email)

    def get_minimum_lesson_price(self, email: str) -> int:
        return self.tutor_ranking_interactor.get_minimum_lesson_price(email)

    def get_tutor_number_of_lessons(self, email: str) -> int:
        return self.tutor_ranking_interactor.get_tutor_number_of_lessons(email)

    def get_admin_score(self, email: str) -> int:
        return self.tutor_ranking_interactor.get_admin_score(email)

    def add_review_score(self, email: str, review_score: int) -> None:
        self.tutor_ranking_interactor.add_review_score(email, review_score)

    def add_number_of_lessons(self, email: str, added_lesson_number: int) -> None:
        self.tutor_ranking_interactor.add_number_of_lessons(email, added_lesson_number)

    def set_minimum_lesson_price(self, email: str, new_price: int) -> None:
        self.tutor_ranking_interactor.set_minimum_lesson_price(email, new_price)

    def set_admin_score(self, email: str, admin_score: int) -> None:
        self.tutor_ranking_interactor.set_admin_score(email, admin_score)

    def sort_by_review_score_desc(self) -> List[str]:
        return self.tutor_ranking_interactor.sort_by_review_score_desc()

    def sort_by_review_score_asc(self) -> List[str]:
        return self.tutor_ranking_interactor.sort_by_review_score_asc()

    def sort_by_number_of_lessons_asc(self) -> List[str]:
        return self.tutor_ranking_interactor.sort_by_number_of_lessons_asc()

    def sort_by_number_of_lessons_desc(self) -> List[str]:
        return self.tutor_ranking_interactor.sort_by_number_of_lessons_desc()

    def sort_by_minimum_lesson_price_asc(self) -> List[str]:
        return self.tutor_ranking_interactor.sort_by_minimum_lesson_price_asc()

    def sort_by_minimum_lesson_price_desc(self) -> List[str]:
        return self.tutor_ranking_interactor.sort_by_minimum_lesson_price_desc()

    def sort_by_admin_score_asc(self) -> List[str]:
        return self.tutor_ranking_interactor.sort_by_admin_score_asc()

    def sort_by_admin_score_desc(self) -> List[str]:
        return self.tutor_ranking_interactor.sort_by_review_score_desc()

    def create_message(
        self, message_text: str, tutor_mail: str, student_mail: str
    ) -> Message:
        return self.message_interactor.create_message(
            message_text, tutor_mail, student_mail
        )

    def get_messages(self, tutor_mail: str, student_mail: str) -> List[Message]:
        return self.message_interactor.get_messages(tutor_mail, student_mail)

    def delete_tutor_messages(self, tutor_mail: str) -> None:
        self.message_interactor.delete_tutor_messages(tutor_mail)

    def delete_student_messages(self, student_mail: str) -> None:
        self.message_interactor.delete_student_messages(student_mail)

    def get_student_messaged_tutors(self, student_mail: str) -> List[str]:
        return self.message_interactor.get_student_messaged_tutors(student_mail)

    def get_tutor_messaged_students(self, tutor_mail: str) -> List[str]:
        return self.message_interactor.get_tutor_messaged_students(tutor_mail)

    def create_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> Homework:
        return self.homework_interactor.create_homework(
            homework_text, tutor_mail, student_mail
        )

    def change_homework(
        self,
        new_homework_text: str,
        old_homework_text: str,
        tutor_mail: str,
        student_mail: str,
    ) -> Homework:
        return self.homework_interactor.change_homework(
            new_homework_text, old_homework_text, tutor_mail, student_mail
        )

    def get_student_homework(self, student_mail: str) -> List[Homework]:
        return self.homework_interactor.get_student_homework(student_mail)

    def delete_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        self.homework_interactor.delete_homework(
            homework_text, tutor_mail, student_mail
        )

    def get_course(self, subject: str, tutor_mail: str) -> Course:
        return self.course_interactor.get_course(subject, tutor_mail)

    def delete_course(self, tutor_mail: str, subject: str) -> None:
        return self.course_interactor.delete_course(tutor_mail, subject)

    def change_price(self, tutor_mail: str, subject: str, course_price: int) -> None:
        return self.course_interactor.change_price(tutor_mail, subject, course_price)

    def create_review(
        self, review_text: str, tutor_mail: str, student_mail: str
    ) -> Review:
        return self.review_interactor.create_review(
            review_text, tutor_mail, student_mail
        )

    def get_review(self, tutor_mail: str, student_mail: str) -> Review:
        return self.review_interactor.get_review(tutor_mail, student_mail)

    def get_tutor_reviews(self, tutor_mail: str) -> List[Review]:
        return self.review_interactor.get_tutor_reviews(tutor_mail)

    def delete_review(self, tutor_mail: str, student_mail: str) -> None:
        self.review_interactor.delete_review(tutor_mail, student_mail)

    def change_review(
        self, new_review_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        self.review_interactor.change_review(new_review_text, tutor_mail, student_mail)

    def create_lesson(
        self,
        subject: str,
        tutor_mail: str,
        student_mail: str,
        number_of_lessons: int,
        lesson_price: int,
    ) -> Lesson:
        return self.lesson_interactor.create_lesson(
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

    def get_tutor_lessons(self, tutor_mail: str) -> List[Lesson]:
        return self.lesson_interactor.get_tutor_lessons(tutor_mail)

    def get_tutor_students(self, tutor_mail: str) -> List[str]:
        return self.lesson_interactor.get_tutor_students(tutor_mail)

    def create_student(
        self, first_name: str, last_name: str, email: str, password: str, balance: int
    ) -> Student:
        return self.student_interactor.create_student(
            first_name, last_name, email, password, balance
        )

    def get_student(self, email: str) -> Student:
        return self.student_interactor.get_student(email)

    def set_student_balance(self, student_mail: str, new_balance: int) -> None:
        self.student_interactor.set_student_balance(student_mail, new_balance)

    def get_student_balance(self, student_mail: str) -> int:
        return self.student_interactor.get_student_balance(student_mail)

    def increase_student_balance(self, student_mail: str, amount: int) -> None:
        self.student_interactor.increase_student_balance(student_mail, amount)

    def decrease_student_balance(self, student_mail: str, amount: int) -> None:
        self.student_interactor.decrease_student_balance(student_mail, amount)

    def change_student_first_name(self, student_mail: str, first_name: str) -> None:
        self.student_interactor.change_student_first_name(student_mail, first_name)

    def change_student_last_name(self, student_mail: str, last_name: str) -> None:
        self.student_interactor.change_student_last_name(student_mail, last_name)

    def delete_student(self, student_mail: str) -> None:
        self.student_interactor.delete_student(student_mail)

    def create_tutor(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        balance: int,
        biography: str,
        profile_address: str = "",
    ) -> Tutor:
        return self.tutor_interactor.create_tutor(
            first_name, last_name, email, password, balance, biography, profile_address
        )

    def get_tutor(self, email: str) -> Tutor:
        return self.tutor_interactor.get_tutor(email)

    def set_tutor_balance(self, tutor_mail: str, new_balance: int) -> None:
        self.tutor_interactor.set_tutor_balance(tutor_mail, new_balance)

    def get_tutor_balance(self, tutor_mail: str) -> int:
        return self.tutor_interactor.get_tutor_balance(tutor_mail)

    def increase_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        self.tutor_interactor.increase_tutor_balance(tutor_mail, amount)

    def decrease_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        self.tutor_interactor.decrease_tutor_balance(tutor_mail, amount)

    def set_commission_pct(self, tutor_mail: str, new_commission_pct: float) -> None:
        self.tutor_interactor.set_commission_pct(tutor_mail, new_commission_pct)

    def decrease_commission_pct(self, tutor_mail: str) -> None:
        self.tutor_interactor.decrease_commission_pct(tutor_mail)

    def change_tutor_first_name(self, tutor_mail: str, first_name: str) -> None:
        self.tutor_interactor.change_tutor_first_name(tutor_mail, first_name)

    def change_tutor_last_name(self, tutor_mail: str, last_name: str) -> None:
        self.tutor_interactor.change_tutor_last_name(tutor_mail, last_name)

    def change_tutor_biography(self, tutor_mail: str, biography: str) -> None:
        self.tutor_interactor.change_tutor_biography(tutor_mail, biography)

    def change_tutor_profile_address(
        self, tutor_mail: str, profile_address: str
    ) -> None:
        self.tutor_interactor.change_tutor_profile_address(tutor_mail, profile_address)

    def delete_tutor(self, tutor_mail: str) -> None:
        self.tutor_interactor.delete_tutor(tutor_mail)

    @classmethod
    def create(
        cls,
        course_interactor: ICourseInteractor,
        review_interactor: IReviewInteractor,
        lesson_interactor: ILessonInteractor,
        student_interactor: IStudentInteractor,
        tutor_interactor: ITutorInteractor,
        homework_interactor: IHomeworkInteractor,
        message_interactor: IMessageInteractor,
        tutor_ranking_interactor: ITutorRankingInteractor,
    ) -> "OlympianTutorService":
        return cls(
            course_interactor=CourseInteractor(course_interactor),
            review_interactor=ReviewInteractor(review_interactor),
            lesson_interactor=LessonInteractor(lesson_interactor),
            student_interactor=StudentInteractor(student_interactor),
            tutor_interactor=TutorInteractor(tutor_interactor),
            homework_interactor=HomeworkInteractor(homework_interactor),
            message_interactor=MessageInteractor(message_interactor),
            tutor_ranking_interactor=TutorRankingInteractor(tutor_ranking_interactor),
        )
