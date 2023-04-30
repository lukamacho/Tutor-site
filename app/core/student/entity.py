from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    password: str
    balance: 0
    profile_address: str = ""
    lessons: Dict[int, int] = field(default_factory=dict)

    def set_balance(self, new_balance: int) -> None:
        self.balance = new_balance

    def get_balance(self) -> int:
        return self.balance

    def increase_balance(self, amount: int) -> None:
        self.balance += amount

    def decrease_balance(self, amount: int) -> None:
        self.balance -= amount

    def change_first_name(self, first_name: str) -> None:
        self.first_name = first_name

    def change_last_name(self, last_name: str) -> None:
        self.last_name = last_name

    def set_student_info(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def add_lessons(self, course_id: int, num_lessons: int) -> None:
        self.lessons[course_id] += num_lessons

    def book_lesson(self, course_id: int, timeslot: str) -> None:
        pass

    def buy_lessons(self, course_id: int, num_lessons: int) -> None:
        pass

    def reschedule_lesson(
        self, course_id: int, old_timeslot: str, new_timeslot: str
    ) -> None:
        pass
