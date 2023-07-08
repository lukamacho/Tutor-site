from dataclasses import dataclass
from typing import List, Protocol

from app.core.review.entity import Review


class IReviewRepository(Protocol):
    def create_review(
        self, review_text: str, tutor_mail: str, student_mail: str
    ) -> Review:
        pass

    def get_review(self, tutor_mail: str, student_mail: str) -> Review:
        pass

    def get_tutor_reviews(self, tutor_mail: str) -> List[Review]:
        pass

    def delete_review(self, tutor_mail: str, student_mail: str) -> None:
        pass

    def change_review(
        self, new_review_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        pass


class IReviewInteractor(Protocol):
    def create_review(
        self, review_text: str, tutor_mail: str, student_mail: str
    ) -> Review:
        pass

    def get_review(self, tutor_mail: str, student_mail: str) -> Review:
        pass

    def get_tutor_reviews(self, tutor_mail: str) -> List[Review]:
        pass

    def delete_review(self, tutor_mail: str, student_mail: str) -> None:
        pass

    def change_review(
        self, new_review_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        pass


@dataclass
class ReviewInteractor:
    review_repository: IReviewRepository

    def create_review(
        self, review_text: str, tutor_mail: str, student_mail: str
    ) -> Review:
        return self.review_repository.create_review(
            review_text, tutor_mail, student_mail
        )

    def get_review(self, tutor_mail: str, student_mail: str) -> Review:
        return self.review_repository.get_review(tutor_mail, student_mail)

    def get_tutor_reviews(self, tutor_mail: str) -> List[Review]:
        return self.review_repository.get_tutor_reviews(tutor_mail)

    def delete_review(self, tutor_mail: str, student_mail: str) -> None:
        self.review_repository.delete_review(tutor_mail, student_mail)

    def change_review(
        self, new_review_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        self.review_repository.change_review(new_review_text, tutor_mail, student_mail)
