from dataclasses import dataclass, field
from typing import Dict, Optional

from app.core.tutor.entity import Tutor


@dataclass
class InMemoryTutorRepository:
    data: Dict[str, Tutor] = field(default_factory=dict)

    def create_tutor(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        balance: int,
        biography: str,
    ) -> Tutor:
        tutor = Tutor(first_name, last_name, email, password, 0.25, balance, biography)
        self.data[email] = tutor
        return tutor

    def get_tutor(self, email: str) -> Optional[Tutor]:
        if email in self.data.keys():
            return self.data[email]
        return None

    def set_tutor_balance(self, tutor_mail: str, new_balance: int) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor is not None:
            tutor.set_balance(new_balance)

    def get_tutor_balance(self, student_mail: str) -> int:
        tutor = self.get_tutor(student_mail)
        if tutor is not None:
            return tutor.get_balance()
        return 0

    def increase_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor is not None:
            return tutor.increase_balance(amount)

    def decrease_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor is not None:
            return tutor.decrease_balance(amount)

    def set_commission_pct(self, tutor_mail: str, new_commission_pct: float):
        tutor = self.get_tutor(tutor_mail)
        if tutor is not None:
            return tutor.set_commission_pct(new_commission_pct)

    def decrease_commission_pct(self, tutor_mail: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor is not None:
            return tutor.decrease_commission_pct()

    def change_tutor_first_name(self, tutor_mail: str, first_name: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor is not None:
            tutor.change_first_name(first_name)

    def change_tutor_last_name(self, tutor_mail: str, last_name: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor is not None:
            tutor.change_last_name(last_name)

    def change_tutor_biography(self, tutor_mail: str, biography: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor is not None:
            tutor.change_biography(biography)
