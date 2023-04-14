import sqlite3
from dataclasses import dataclass
from typing import Optional

from app.core.student.entity import Student


@dataclass
class SQLStudentRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists Students (
                first_name TEXT,
                last_name TEXT,
                email TEXT primary key,
                balance INTEGER
            );
            """
        )
        self.conn.commit()

    def create_student(
        self, first_name: str, last_name: str, email: str, balance: int
    ) -> Student:
        self.conn.execute(
            " INSERT INTO Students VALUES (?,?,?,?)",
            (first_name, last_name, email, balance),
        )
        self.conn.commit()
        return Student(first_name, last_name, email, balance)

    def get_student(self, email: str) -> Optional[Student]:
        for row in self.conn.execute(
            " SELECT * FROM Students WHERE email = ?", (email,)
        ):
            return Student(*row)

        return None
