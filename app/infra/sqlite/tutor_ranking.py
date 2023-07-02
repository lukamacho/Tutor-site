import sqlite3
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SqlTutorRankingRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists TutorRankings (
                email TEXT primary key,
                review_scores int,
                number_of_reviews int,
                number_of_lessons int,
                minimum_lesson_price int,
                admin_score int,
                FOREIGN KEY (email) REFERENCES Tutors (email)          
            );
            """
        )
        self.conn.commit()

    def add_tutor_in_ranking(
        self,
        email: str,
    ) -> None:
        review_scores = 0
        number_of_reviews = 0
        number_of_lessons = 0
        minimum_lesson_price = 1000000000
        admin_evaluation = 0
        self.conn.execute(
            " INSERT INTO TutorRankings VALUES (?,?,?,?,?,?)",
            (
                email,
                review_scores,
                number_of_reviews,
                number_of_lessons,
                minimum_lesson_price,
                admin_evaluation,
            ),
        )
        self.conn.commit()
        print("Tutor has been added in the tutor rankings.")

    def get_review_scores(self, email: str) -> int:
        for row in self.conn.execute(
            " SELECT review_scores FROM TutorRankings WHERE email = ?",
            (email,),
        ):
            return int(*row)

        return 0

    def get_number_of_reviews(self, email: str) -> int:
        for row in self.conn.execute(
            " SELECT number_of_reviews FROM TutorRankings WHERE email = ?",
            (email,),
        ):
            return int(*row)

        return 0

    def get_minimum_lesson_price(self, email: str) -> int:
        for row in self.conn.execute(
            " SELECT minimum_lesson_price FROM TutorRankings WHERE email = ?",
            (email,),
        ):
            return int(*row)

        return 0

    def get_number_of_lessons(self, email: str) -> int:
        for row in self.conn.execute(
            " SELECT number_of_lessons FROM TutorRankings WHERE email = ?",
            (email,),
        ):
            return int(*row)

        return 0

    def get_admin_score(self, email: str) -> int:
        for row in self.conn.execute(
            " SELECT admin_score FROM TutorRankings WHERE email = ?",
            (email,),
        ):
            return int(*row)

        return 0

    def add_review_score(self, email: str, review_score: int) -> None:
        review_scores = self.get_review_scores(email)
        review_scores += review_score
        number_of_reviews = self.get_number_of_reviews(email)
        number_of_reviews += 1
        self.conn.execute(
            "UPDATE TutorRankings SET review_scores = ?, number_of_reviews = ?  WHERE email = ?",
            (
                review_scores,
                number_of_reviews,
                email,
            ),
        )
        self.conn.commit()

    def add_number_of_lessons(self, email: str, added_lesson_number: int) -> None:
        number_of_lessons = self.get_number_of_lessons(email)
        new_number_of_lessons = number_of_lessons + added_lesson_number
        self.conn.execute(
            "UPDATE TutorRankings SET number_of_lessons = ?  WHERE email = ?",
            (
                new_number_of_lessons,
                email,
            ),
        )
        self.conn.commit()

    def set_minimum_lesson_price(self, email: str, new_price: int) -> None:
        current_minimum_price = self.get_minimum_lesson_price(email)
        new_minimum_price = min(current_minimum_price, new_price)
        self.conn.execute(
            "UPDATE TutorRankings SET minimum_lesson_price = ?  WHERE email = ?",
            (
                new_minimum_price,
                email,
            ),
        )
        self.conn.commit()

    def set_admin_score(self, email: str, admin_score: int) -> None:
        self.conn.execute(
            "UPDATE TutorRankings SET admin_score = ?  WHERE email = ?",
            (
                admin_score,
                email,
            ),
        )
        self.conn.commit()

    def sort_by_review_score_desc(self) -> List[str]:
        tutor_mails: List[str] = []
        for row in self.conn.execute(
            "SELECT email FROM TutorRankings ORDER BY CAST(review_scores AS REAL) / NULLIF(number_of_reviews, 0) DESC"
        ):
            tutor_mails.append(row[0])
        return tutor_mails

    def sort_by_review_score_asc(self) -> List[str]:
        tutor_mails: List[str] = []
        for row in self.conn.execute(
            "SELECT email FROM TutorRankings ORDER BY CAST(review_scores AS REAL) / NULLIF(number_of_reviews, 0) ASC"
        ):
            tutor_mails.append(row[0])
        return tutor_mails

    def sort_by_number_of_lessons_asc(self) -> List[str]:
        tutor_mails: List[str] = []
        for row in self.conn.execute(
            "SELECT email FROM TutorRankings ORDER BY number_of_lessons ASC"
        ):
            tutor_mails.append(row[0])
        return tutor_mails

    def sort_by_number_of_lessons_desc(self) -> List[str]:
        tutor_mails: List[str] = []
        for row in self.conn.execute(
            "SELECT email FROM TutorRankings ORDER BY number_of_lessons DESC"
        ):
            tutor_mails.append(row[0])
        return tutor_mails

    def sort_by_minimum_lesson_price_asc(self) -> List[str]:
        tutor_mails: List[str] = []
        for row in self.conn.execute(
            "SELECT email FROM TutorRankings ORDER BY minimum_lesson_price ASC"
        ):
            tutor_mails.append(row[0])
        return tutor_mails

    def sort_by_minimum_lesson_price_desc(self) -> List[str]:
        tutor_mails: List[str] = []
        for row in self.conn.execute(
            "SELECT email FROM TutorRankings ORDER BY minimum_lesson_price DESC"
        ):
            tutor_mails.append(row[0])
        return tutor_mails

    def sort_by_admin_score_asc(self) -> List[str]:
        tutor_mails: List[str] = []
        for row in self.conn.execute(
            "SELECT email FROM TutorRankings ORDER BY admin_score ASC"
        ):
            tutor_mails.append(row[0])
        return tutor_mails

    def sort_by_admin_score_desc(self) -> List[str]:
        tutor_mails: List[str] = []
        for row in self.conn.execute(
            "SELECT email FROM TutorRankings ORDER BY admin_score DESC"
        ):
            tutor_mails.append(row[0])
        return tutor_mails
