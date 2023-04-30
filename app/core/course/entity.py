from dataclasses import dataclass


@dataclass
class Course:
    subject: str
    tutor_mail: str
    price: int

    def set_course_info(self, subject: str, tutor_mail: str, price: int) -> None:
        self.subject = subject
        self.tutor_mail = tutor_mail
        self.price = price
