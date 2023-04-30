import sqlite3
from dataclasses import dataclass
from typing import Optional, List

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

    def get_course(self, subject: str, tutor_mail: str) -> Optional[Course]:
        for row in self.conn.execute(
            " SELECT * FROM Courses WHERE subject = ? and tutor_mail = ?",
            (
                subject,
                tutor_mail,
            ),
        ):
            return Course(*row)

        return None

    def get_courses(self, tutor_mail: str) -> Optional[List[Course]]:
        courses: List[Course] = []
        for row in self.conn.execute(
            " SELECT * FROM Courses WHERE tutor_mail = ?", (tutor_mail,)
        ):
            courses.append(Course(*row))

        return courses
