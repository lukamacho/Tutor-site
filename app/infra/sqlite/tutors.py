import sqlite3
from dataclasses import dataclass
from typing import Optional

from app.core.tutor.entity import Tutor


@dataclass
class SqlTutorRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists Tutors (
                first_name TEXT ,
                last_name TEXT ,
                email TEXT primary key,
                password TEXT NOT NULL,
                commission_pct REAL NOT NULL
                balance INTEGER,
                biography TEXT,
            );
            """
        )
        self.conn.commit()

    def create_tutor(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        balance: int,
        biography: str,
    ) -> Tutor:
        commission_pct = 0.25
        self.conn.execute(
            " INSERT INTO Tutors VALUES (?,?,?,?,?,?,?)",
            (
                first_name,
                last_name,
                email,
                password,
                commission_pct,
                balance,
                biography,
            ),
        )
        self.conn.commit()
        return Tutor(
            first_name, last_name, email, password, commission_pct, balance, biography
        )

    def get_tutor(self, email: str) -> Optional[Tutor]:
        for row in self.conn.execute(" SELECT * FROM Tutors WHERE email = ?", (email,)):
            return Tutor(*row)

        return None

    def set_balance(self, tutor_mail: str, new_balance: int) -> None:
        self.conn.execute(
            "UPDATE Tutors SET balance = ? WHERE email = ? ",
            (
                new_balance,
                tutor_mail,
            ),
        )
        self.conn.commit()

    def get_balance(self, student_mail: str) -> int:
        tutor = self.get_tutor(student_mail)
        if tutor is None:
            return 0
        return tutor.balance

    def increase_balance(self, tutor_mail: str, amount: int) -> None:
        current_balance = self.get_balance(tutor_mail)
        new_balance = current_balance + amount
        self.set_balance(tutor_mail, new_balance)

    def decrease_balance(self, tutor_mail: str, amount: int) -> None:
        current_balance = self.get_balance(tutor_mail)
        new_balance = current_balance - amount
        self.set_balance(tutor_mail, new_balance)

    def set_commission_pct(self, tutor_mail: str, new_commission_pct: float):
        self.conn.execute(
            "UPDATE Tutors SET commission_pct = ? WHERE email = ? ",
            (
                new_commission_pct,
                tutor_mail,
            ),
        )
        self.conn.commit()

    def decrease_commission_pct(self, tutor_mail: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        commission_pct = tutor.commission_pct
        new_commission_pct = commission_pct - 1
        self.set_commission_pct(tutor_mail, new_commission_pct)

    def change_first_name(self, tutor_mail: str, first_name: str) -> None:
        self.conn.execute(
            "UPDATE Tutors SET  first_name = ? WHERE email = ? ",
            (
                first_name,
                tutor_mail,
            ),
        )
        self.conn.commit()

    def change_last_name(self, tutor_mail: str, last_name: str) -> None:
        self.conn.execute(
            "UPDATE Tutors SET  last_name = ? WHERE email = ? ",
            (
                last_name,
                tutor_mail,
            ),
        )
        self.conn.commit()

    def change_biography(self, tutor_mail: str, biography: str) -> None:
        self.conn.execute(
            "UPDATE Tutors SET  biography = ? WHERE email = ? ",
            (
                biography,
                tutor_mail,
            ),
        )
        self.conn.commit()