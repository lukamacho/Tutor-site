import sqlite3
from dataclasses import dataclass
from typing import Optional

from app.core.tutor.entity import Tutor


@dataclass
class SQLTutorRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists Tutors (
                first_name TEXT,
                last_name TEXT,
                email TEXT primary key,
                balance INTEGER,
                biography TEXT,
            );
            """
        )
        self.conn.commit()

    def create_tutor(
        self, first_name: str, last_name: str, email: str, balance: int, biography: str
    ) -> Tutor:
        self.conn.execute(
            " INSERT INTO Tutors VALUES (?,?,?,?,?)",
            (first_name, last_name, email, balance, biography),
        )
        self.conn.commit()
        return Tutor(first_name, last_name, email, balance)

    def get_tutor(self, email: str) -> Optional[Tutor]:
        for row in self.conn.execute(" SELECT * FROM Tutors WHERE email = ?", (email,)):
            return Tutor(*row)

        return None
