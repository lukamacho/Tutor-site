from dataclasses import dataclass


@dataclass
class Lesson:
    subject: str
    tutor_mail: str
    student_mail: str
    number_of_lessons: str
    lesson_price: int
