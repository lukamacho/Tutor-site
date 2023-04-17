import sqlite3
from dataclasses import dataclass
from typing import Optional

from app.core.course.entity import Course
from app.core.lesson.entity import Lesson


@dataclass
class SqlLessonRepository:
    def __init__(self, filename: str) -> None:
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.executescript(
            """
            create table if not exists Courses (
                subject TEXT NOT NULL,
                tutor_mail TEXT NOT NULL,
                student_mail TEXT NOT NULL,
                number_of_lessons int,
                lesson_price int,
                FOREIGN KEY (tutor_mail) REFERENCES Tutors (email),
                FOREIGN KEY (student_mail) REFERENCES Students (email)  
            );
            """
        )
        self.conn.commit()

    def create_lesson(
        self,
        subject: str,
        tutor_mail: str,
        student_mail: str,
        number_of_lessons: int,
        lesson_price: int,
    ) -> Lesson:
        self.conn.execute(
            " INSERT INTO Lessons VALUES (?,?,?,?,?)",
            (subject, tutor_mail, student_mail, number_of_lessons, lesson_price),
        )
        self.conn.commit()
        return Lesson(
            subject, tutor_mail, student_mail, number_of_lessons, lesson_price
        )

    def get_lesson(self, tutor_mail: str, student_mail: str, subject: str) -> Lesson:
        for row in self.conn.execute(
            " SELECT * FROM Lessons WHERE tutor_mail = ? and student_mail = ? and subject = ?",
            (tutor_mail, student_mail, subject),
        ):
            return Lesson(*row)

        return None

    def get_number_of_lessons(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> int:
        lesson = self.get_lesson(tutor_mail, student_mail, subject)
        return lesson.number_of_lessons

    def set_number_of_lessons(
        self, tutor_mail: str, student_mail: str, new_number: int, subject: str
    ) -> None:
        self.conn.execute(
            "UPDATE Lessons SET number_of_lessons = ? WHERE tutor_mail = ? and student_mail = ? and subject = ?",
            (
                new_number,
                tutor_mail,
                student_mail,
                subject,
            ),
        )
        self.conn.commit()

    def decrease_lesson_number(
        self, tutor_mail: str, student_mail: str, subject: str
    ) -> None:
        number_of_lessons = self.get_number_of_lessons(
            tutor_mail, student_mail, subject
        )
        number_of_lessons = number_of_lessons - 1
        self.set_number_of_lessons(tutor_mail, student_mail, number_of_lessons, subject)

    def increase_lesson_number(
        self, tutor_mail: str, student_mail: str, added_lessons, subject: str
    ) -> None:
        number_of_lessons = self.get_number_of_lessons(
            tutor_mail, student_mail, subject
        )
        number_of_lessons = number_of_lessons + added_lessons
        self.set_number_of_lessons(tutor_mail, student_mail, number_of_lessons, subject)

    def set_lesson_price(
        self, tutor_mail: str, student_mail: str, subject: str, new_price: int
    ) -> None:
        self.conn.execute(
            "UPDATE Lessons SET lesson_price = ? WHERE tutor_mail = ? and student_mail = ? and subject = ?",
            (
                new_price,
                tutor_mail,
                student_mail,
                subject,
            ),
        )
        self.conn.commit()
