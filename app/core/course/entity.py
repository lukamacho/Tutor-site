from dataclasses import dataclass


@dataclass
class Course:
    subject: str
    tutor_mail: str
    price: int
