import sqlite3
from dataclasses import dataclass
from typing import Optional

from app.core.student.entity import Student


@dataclass
class SqlStudentRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists Students (
                first_name TEXT,
                last_name TEXT,
                email TEXT primary key,
                password TEXT NOT NULL,
                balance INTEGER,
                profile_address TEXT
            );
            """
        )
        self.conn.commit()

    def create_student(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        balance: int,
        profile_address: str = "",
    ) -> Student:
        self.conn.execute(
            " INSERT INTO Students VALUES (?,?,?,?,?,?)",
            (
                first_name,
                last_name,
                email,
                password,
                balance,
                profile_address,
            ),
        )
        self.conn.commit()
        print("Student has been created.")
        return Student(first_name, last_name, email, password, balance, profile_address)

    def get_student(self, email: str) -> Optional[Student]:
        for row in self.conn.execute(
            " SELECT * FROM Students WHERE email = ?", (email,)
        ):
            return Student(*row)

        return None

    def set_student_balance(self, student_mail: str, new_balance: int) -> None:
        self.conn.execute(
            "UPDATE Students SET balance = ? WHERE email = ? ",
            (
                new_balance,
                student_mail,
            ),
        )
        self.conn.commit()

    def get_student_balance(self, student_mail: str) -> int:
        student = self.get_student(student_mail)
        if student is None:
            return 0
        return student.balance

    def increase_student_balance(self, student_mail: str, amount: int) -> None:
        current_balance = self.get_student_balance(student_mail)
        new_balance = current_balance + amount
        self.set_student_balance(student_mail, new_balance)

    def decrease_student_balance(self, student_mail: str, amount: int) -> None:
        current_balance = self.get_student_balance(student_mail)
        new_balance = current_balance - amount
        self.set_student_balance(student_mail, new_balance)

    def change_student_first_name(self, student_mail: str, first_name: str) -> None:
        self.conn.execute(
            "UPDATE Students SET  first_name = ? WHERE email = ? ",
            (
                first_name,
                student_mail,
            ),
        )
        self.conn.commit()

    def change_student_last_name(self, student_mail: str, last_name: str) -> None:
        self.conn.execute(
            "UPDATE Students SET last_name = ? WHERE email = ? ",
            (
                last_name,
                student_mail,
            ),
        )
        self.conn.commit()

    def change_student_password(self, student_mail: str, password: str) -> None:
        self.conn.execute(
            "UPDATE Students SET  password = ? WHERE email = ? ",
            (
                password,
                student_mail,
            ),
        )
        self.conn.commit()

    def change_student_profile_address(self, student_mail: str, profile_address: str) -> None:
        self.conn.execute(
            "UPDATE Students SET profile_address = ? WHERE email = ? ",
            (
                profile_address,
                student_mail,
            ),
        )
        self.conn.commit()

    def delete_student(self, student_mail: str) -> None:
        self.conn.execute(
            "DELETE FROM Students WHERE  email = ?  ",
            (student_mail,),
        )
        self.conn.commit()
