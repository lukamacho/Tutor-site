from dataclasses import dataclass

from app.infra.inmemory.tutor import Tutor


@dataclass
class Admin:
    def add_balance(self, user_id: int, amount: int) -> None:
        pass

    def decrease_balance(self, tutor_id: int, amount: int) -> None:
        pass

    def delete_user(self, tutor_or_user_id) -> None:
        pass

    def set_top_tutor(self, tutor_id) -> None:
        Tutor.is_top_tutor = True
        pass

    def send_message(self, tutor_or_user_id) -> None:
        pass

    def reschedule_lesson(self, lesson_id) -> None:
        pass
