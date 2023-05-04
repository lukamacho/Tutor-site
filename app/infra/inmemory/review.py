from dataclasses import dataclass, field
from typing import List, Optional

from app.core.review.entity import Review


@dataclass
class InMemoryReviewRepository:
    data: List[Review] = field(default_factory=list)

    def create_review(
        self, review_text: str, tutor_mail: str, student_mail: str
    ) -> Review:
        review = Review(review_text, tutor_mail, student_mail)
        self.data.append(review)
        return review

    def get_review(self, tutor_mail: str, student_mail: str) -> Optional[Review]:
        for review in self.data:
            if review.tutor_mail == tutor_mail and review.student_mail == student_mail:
                return review
        return None

    def get_tutor_reviews(self, tutor_mail: str) -> List[Review]:
        reviews: List[Review] = []
        for review in self.data:
            if review.tutor_mail == tutor_mail:
                reviews.append(review)
        return reviews

    def delete_review(self, tutor_mail: str, student_mail: str) -> None:
        i = 0
        length = len(self.data)

        while i < length:
            review = self.data[i]
            if review.tutor_mail == tutor_mail and review.student_mail == student_mail:
                self.data.remove(review)
                i -= 1
                length -= 1
            i += 1

    def change_review(
        self, new_review_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        for review in self.data:
            if review.tutor_mail == tutor_mail and review.student_mail == student_mail:
                review.review_text = new_review_text
