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
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT primary key,
                balance INTEGER,
                biography TEXT NOT NULL,
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

    def get_tutor_balance(self, email: str) -> int:
        tutor = self.get_tutor(email)
        return tutor.balance

    def set_tutor_balance(self, email: str, new_balance: int) -> None:
        self.conn.execute(
            "UPDATE Tutors SET balance = ? WHERE email = ?",
            (
                new_balance,
                email,
            ),
        )
        self.conn.commit()

    def decrease_balance(self, email: str, amount: int) -> None:
        current_balance = self.get_tutor_balance(email)
        new_balance = current_balance - amount
        self.set_tutor_balance(new_balance)

    def increase_balance(self, email: str, amount: int) -> None:
        current_balance = self.get_tutor_balance(email)
        new_balance = current_balance + amount
        self.set_tutor_balance(new_balance)
