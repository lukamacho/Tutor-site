import sqlite3
from dataclasses import dataclass

from app.core.review.entity import Review


@dataclass
class SqlTReviewRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists Reviews (
                review_text TEXT NOT NULL,
                tutor_mail TEXT,
                student_mail TEXT,
                FOREIGN KEY (tutor_mail) REFERENCES Tutors (email),
                FOREIGN KEY (student_mail) REFERENCES Students (email)  
            );
            """
        )
        self.conn.commit()

    def create_review(
        self, review_text: str, tutor_mail: str, student_mail: str
    ) -> Review:
        self.conn.execute(
            " INSERT INTO Reviews VALUES (?,?,?)",
            (
                review_text,
                tutor_mail,
                student_mail,
            ),
        )
        self.conn.commit()
        return Review(review_text, tutor_mail, student_mail)

    def get_review(self, tutor_mail: str, student_mail: str) -> Optional[Review]:
        for row in self.conn.execute(
            " SELECT * FROM Reviews WHERE tutor_mail = ? and student_mail = ?",
            (tutor_mail, student_mail,),
        ):
            return Review(*row)

        return None

    def delete_review(self, tutor_mail: str, student_mail: str) -> None:
        self.conn.execute(
            " DELETE FROM Reviews where tutor_mail = ? and student_mail = ? ",
            (
                tutor_mail,
                student_mail,
            ),
        )
        self.conn.commit()

    def change_review(
        self, new_review_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        self.conn.execute(
            " UPDATE Reviews SET review_text = ? WHERE tutor_mail = ? and student_mail = ? ",
            (
                new_review_text,
                tutor_mail,
                student_mail,
            ),
        )
        self.conn.commit()
