from dataclasses import dataclass
from typing import List, Optional, Protocol


class ITutorRankingInteractor(Protocol):
    def add_tutor_in_ranking(
        self,
        email: str,
    ) -> None:
        pass

    def get_review_scores(self, email: str) -> int:
        pass

    def get_number_of_reviews(self, email: str) -> int:
        pass

    def get_minimum_lesson_price(self, email: str) -> int:
        pass

    def get_number_of_lessons(self, email: str) -> int:
        pass

    def get_admin_score(self, email: str) -> int:
        pass

    def add_review_score(self, email: str, review_score: int) -> None:
        pass

    def add_number_of_lessons(self, email: str, addited_lesson_number: int) -> None:
        pass

    def set_minimum_lesson_price(self, email: str, new_price: int) -> None:
        pass

    def set_admin_score(self, email: str, admin_score: int) -> None:
        pass

    def sort_by_review_score_desc(self) -> List[str]:
        pass

    def sort_by_review_score_asc(self) -> List[str]:
        pass

    def sort_by_number_of_lessons_asc(self) -> List[str]:
        pass

    def sort_by_number_of_lessons_desc(self) -> List[str]:
        pass

    def sort_by_minimum_lesson_price_asc(self) -> List[str]:
        pass

    def sort_by_minimum_lesson_price_desc(self) -> List[str]:
        pass

    def sort_by_admin_score_asc(self) -> List[str]:
        pass

    def sort_by_admin_score_desc(self) -> List[str]:
        pass


class ITutorRankingRepository(Protocol):
    def add_tutor_in_ranking(
        self,
        email: str,
    ) -> None:
        pass

    def get_review_scores(self, email: str) -> int:
        pass

    def get_number_of_reviews(self, email: str) -> int:
        pass

    def get_minimum_lesson_price(self, email: str) -> int:
        pass

    def get_number_of_lessons(self, email: str) -> int:
        pass

    def get_admin_score(self, email: str) -> int:
        pass

    def add_review_score(self, email: str, review_score: int) -> None:
        pass

    def add_number_of_lessons(self, email: str, addited_lesson_number: int) -> None:
        pass

    def set_minimum_lesson_price(self, email: str, new_price: int) -> None:
        pass

    def set_admin_score(self, email: str, admin_score: int) -> None:
        pass

    def sort_by_review_score_desc(self) -> List[str]:
        pass

    def sort_by_review_score_asc(self) -> List[str]:
        pass

    def sort_by_number_of_lessons_asc(self) -> List[str]:
        pass

    def sort_by_number_of_lessons_desc(self) -> List[str]:
        pass

    def sort_by_minimum_lesson_price_asc(self) -> List[str]:
        pass

    def sort_by_minimum_lesson_price_desc(self) -> List[str]:
        pass

    def sort_by_admin_score_asc(self) -> List[str]:
        pass

    def sort_by_admin_score_desc(self) -> List[str]:
        pass


@dataclass
class TutorRankingInteractor:
    tutor_ranking_repository: ITutorRankingRepository

    def add_tutor_in_ranking(
        self,
        email: str,
    ) -> None:
        self.tutor_ranking_repository.add_tutor_in_ranking(email)

    def get_review_scores(self, email: str) -> int:
        return self.tutor_ranking_repository.get_review_scores(email)

    def get_number_of_reviews(self, email: str) -> int:
        return self.tutor_ranking_repository.get_number_of_reviews(email)

    def get_minimum_lesson_price(self, email: str) -> int:
        return self.tutor_ranking_repository.get_minimum_lesson_price(email)

    def get_number_of_lessons(self, email: str) -> int:
        return self.tutor_ranking_repository.get_number_of_lessons(email)

    def get_admin_score(self, email: str) -> int:
        return self.tutor_ranking_repository.get_admin_score(email)

    def add_review_score(self, email: str, review_score: int) -> None:
        self.tutor_ranking_repository.add_review_score(email, review_score)

    def add_number_of_lessons(self, email: str, added_lesson_number: int) -> None:
        self.tutor_ranking_repository.add_number_of_lessons(email, added_lesson_number)

    def set_minimum_lesson_price(self, email: str, new_price: int) -> None:
        self.tutor_ranking_repository.set_minimum_lesson_price(email, new_price)

    def set_admin_score(self, email: str, admin_score: int) -> None:
        self.tutor_ranking_repository.set_admin_score(email, admin_score)

    def sort_by_review_score_desc(self) -> List[str]:
        return self.tutor_ranking_repository.sort_by_review_score_desc()

    def sort_by_review_score_asc(self) -> List[str]:
        return self.tutor_ranking_repository.sort_by_review_score_asc()

    def sort_by_number_of_lessons_asc(self) -> List[str]:
        return self.tutor_ranking_repository.sort_by_number_of_lessons_asc()

    def sort_by_number_of_lessons_desc(self) -> List[str]:
        return self.tutor_ranking_repository.sort_by_number_of_lessons_desc()

    def sort_by_minimum_lesson_price_asc(self) -> List[str]:
        return self.tutor_ranking_repository.sort_by_minimum_lesson_price_asc()

    def sort_by_minimum_lesson_price_desc(self) -> List[str]:
        return self.tutor_ranking_repository.sort_by_minimum_lesson_price_desc()

    def sort_by_admin_score_asc(self) -> List[str]:
        return self.tutor_ranking_repository.sort_by_admin_score_asc()

    def sort_by_admin_score_desc(self) -> List[str]:
        return self.tutor_ranking_repository.sort_by_review_score_desc()
