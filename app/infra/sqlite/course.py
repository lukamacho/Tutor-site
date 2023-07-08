import sqlite3
from dataclasses import dataclass
from typing import List

from app.core.course.entity import Course


@dataclass
class SqlCourseRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists Courses (
                subject TEXT,
                tutor_mail TEXT,
                price INTEGER
            );
            """
        )
        self.conn.commit()

    def create_course(self, subject: str, tutor_mail: str, price: int) -> Course:
        self.conn.execute(
            " INSERT INTO Courses VALUES (?,?,?)",
            (subject, tutor_mail, price),
        )
        self.conn.commit()
        return Course(subject, tutor_mail, price)

    def get_course(self, subject: str, tutor_mail: str) -> Course:
        for row in self.conn.execute(
            " SELECT * FROM Courses WHERE subject = ? and tutor_mail = ?",
            (
                subject,
                tutor_mail,
            ),
        ):
            return Course(*row)

        return Course("", "", 0)

    def get_tutor_courses(self, tutor_mail: str) -> List[Course]:
        courses: List[Course] = []
        for row in self.conn.execute(
            " SELECT * FROM Courses WHERE tutor_mail = ?", (tutor_mail,)
        ):
            courses.append(Course(*row))

        return courses

    def get_courses(self) -> List[Course]:
        courses: List[Course] = []
        for row in self.conn.execute(
            " SELECT * FROM Courses",
        ):
            courses.append(Course(*row))

        return courses

    def delete_course(self, tutor_mail: str, subject: str) -> None:
        self.conn.execute(
            "DELETE FROM Courses WHERE  tutor_mail = ?  and subject =? ",
            (tutor_mail, subject),
        )
        self.conn.commit()

    def change_price(self, tutor_mail: str, subject: str, course_price: int) -> None:
        self.conn.execute(
            "UPDATE Courses SET price = ? WHERE tutor_mail = ? and subject = ? ",
            (course_price, tutor_mail, subject),
        )
        self.conn.commit()
