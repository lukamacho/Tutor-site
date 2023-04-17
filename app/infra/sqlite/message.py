import sqlite3
from dataclasses import dataclass
from typing import List

from app.core.message.entity import Message


@dataclass
class SqlHomeworkRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists Messages (
                message_text TEXT NOT NULL,
                tutor_mail TEXT NOT NULL,
                student_mail TEXT NOT NULL,
                FOREIGN KEY (tutor_mail) REFERENCES Tutors (email),
                FOREIGN KEY (student_mail) REFERENCES Students (email)  
            );
            """
        )
        self.conn.commit()

    def create_message(
        self, message_text: str, tutor_mail: str, student_mail: str
    ) -> Message:
        self.conn.execute(
            " INSERT INTO Messages VALUES (?,?,?)",
            (
                message_text,
                tutor_mail,
                student_mail,
            ),
        )
        self.conn.commit()
        return Message(message_text, tutor_mail, student_mail)

    def get_messages(self, tutor_mail: str, student_mail: str) -> List[Message]:
        messages = List[Message]
        for row in self.conn.execute(
            " SELECT * FROM Messages WHERE tutor_mail = ? and student_mail = ?",
            (tutor_mail, student_mail),
        ):
            messages.append(*row)

        return messages

    def delete_tutor_messages(
            self, tutor_mail: str
    ) -> None:
        self.conn.execute(
            "DELETE FROM TABLE Messages WHERE  tutor_mail = ?  ",
            (
                tutor_mail,
            ),
        )
        self.conn.commit()

    def delete_student_messages(
            self, student_mail: str
    ) -> None:
        self.conn.execute(
            "DELETE FROM TABLE Messages WHERE  student_mail = ?  ",
            (
                student_mail,
            ),
        )
        self.conn.commit()