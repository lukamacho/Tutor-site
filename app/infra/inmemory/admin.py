from dataclasses import dataclass, field
from typing import Dict, Optional

from app.core.tutor.entity import Tutor


@dataclass
class Admin:
    def add_balance(self, user_id: int, amount: int) -> None:
        pass

    def decrease_balance(self, tutor_id: int, amount: int) -> None:
        pass

    def delete_user(self, tutor_or_user_id: int) -> None:
        pass

    def set_top_tutor(self, tutor_id: int) -> None:
        Tutor.is_top_tutor = True
        pass

    def send_message(self, tutor_or_user_id: int) -> None:
        pass

    def reschedule_lesson(self, lesson_id: int) -> None:
        pass
