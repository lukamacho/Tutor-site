from dataclasses import dataclass


@dataclass
class Lesson:
    subject: str
    tutor_mail: str
    student_mail: str
    number_of_lessons: int
    lesson_price: int
