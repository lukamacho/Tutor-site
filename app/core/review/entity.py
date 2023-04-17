from dataclasses import dataclass


@dataclass
class Review:
    review_text: str
    tutor_mail: str
    student_mail: str
