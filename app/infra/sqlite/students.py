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
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                password TEXT NOT NULL,
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

    def get_student_balance(self, email: str) -> int:
        student = self.get_student(email)
        return student.balance

    def set_student_balance(self, email: str, new_balance: int) -> None:
        self.conn.execute(
            "UPDATE Students SET balance = ? WHERE email = ?",
            (
                new_balance,
                email,
            ),
        )
        self.conn.commit()

    def decrease_balance(self, email: str, amount: int) -> None:
        current_balance = self.get_student_balance(email)
        new_balance = current_balance - amount
        self.set_student_balance(new_balance)

    def increase_balance(self, email: str, amount: int) -> None:
        current_balance = self.get_student_balance(email)
        new_balance = current_balance + amount
        self.set_student_balance(new_balance)
