import sqlite3
from dataclasses import dataclass
from typing import List

from app.core.homework.entity import Homework


@dataclass
class SqlHomeworkRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists Homeworks (
                homework_text TEXT NOT NULL,
                tutor_mail TEXT NOT NULL,
                student_mail TEXT NOT NULL,
                FOREIGN KEY (tutor_mail) REFERENCES Tutors (email),
                FOREIGN KEY (student_mail) REFERENCES Students (email)  
            );
            """
        )
        self.conn.commit()

    def create_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> Homework:
        self.conn.execute(
            " INSERT INTO Homeworks VALUES (?,?,?)",
            (
                homework_text,
                tutor_mail,
                student_mail,
            ),
        )
        self.conn.commit()
        return Homework(homework_text, tutor_mail, student_mail)

    def change_homework(
        self,
        new_homework_text: str,
        old_homework_text: str,
        tutor_mail: str,
        student_mail: str,
    ) -> Homework:
        self.conn.execute(
            "UPDATE Homeworks SET homework_text = ? WHERE tutor_mail = ? and student_mail = ? and homework_text = ?",
            (
                new_homework_text,
                tutor_mail,
                student_mail,
                old_homework_text,
            ),
        )
        self.conn.commit()
        return Homework(new_homework_text, tutor_mail, student_mail)

    def get_student_homework(self, student_mail: str) -> List[Homework]:
        homeworks: List[Homework] = []
        for row in self.conn.execute(
            " SELECT * FROM Homeworks WHERE student_mail = ?", (student_mail,)
        ):
            homeworks.append(Homework(*row))

        return homeworks

    def delete_homework(
        self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        self.conn.execute(
            "DELETE FROM Homeworks WHERE homework_text = ? and tutor_mail = ? and student_mail = ? ",
            (
                homework_text,
                tutor_mail,
                student_mail,
            ),
        )
        self.conn.commit()
