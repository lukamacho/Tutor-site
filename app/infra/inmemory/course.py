from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Course:
    subject: int
    tutor: int
    price: int

    def set_course_info(self, subject_id: int, tutor_id: int, price: int) -> None:
        self.subject = subject_id
        self.tutor = tutor_id
        self.price = price