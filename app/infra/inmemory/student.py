from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Student:
    first_name: str
    last_name: str
    current_balance: 0
    lessons: Dict[int, int] = field(default_factory=dict)

    def set_student_info(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def add_lessons(self, course_id: int, num_lessons: int) -> None:
        self.lessons[course_id] += num_lessons

    def book_lesson(self, course_id: int, timeslot: str) -> None:
        pass

    def buy_lessons(self, course_id: int, num_lessons: int) -> None:
        pass

    def reschedule_lesson(self, course_id: int, old_timeslot: str, new_timeslot: str) -> None:
        pass