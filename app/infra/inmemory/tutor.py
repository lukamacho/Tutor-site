from dataclasses import dataclass, field
from typing import Dict, List

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

    def get_tutor(self, email: str) -> Tutor:
        if email in self.data.keys():
            return self.data[email]
        return Tutor("", "", "", "", 0.0, 0, "", "")

    def set_tutor_balance(self, tutor_mail: str, new_balance: int) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            tutor.set_balance(new_balance)

    def get_tutor_balance(self, student_mail: str) -> int:
        tutor = self.get_tutor(student_mail)
        if tutor.email != "":
            return tutor.get_balance()
        return 0

    def increase_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            return tutor.increase_balance(amount)

    def decrease_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            return tutor.decrease_balance(amount)

    def set_commission_pct(self, tutor_mail: str, new_commission_pct: float) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            return tutor.set_commission_pct(new_commission_pct)

    def decrease_commission_pct(self, tutor_mail: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            return tutor.decrease_commission_pct()

    def change_tutor_first_name(self, tutor_mail: str, first_name: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            tutor.change_first_name(first_name)

    def change_tutor_last_name(self, tutor_mail: str, last_name: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            tutor.change_last_name(last_name)

    def change_tutor_password(self, tutor_mail: str, password: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            tutor.change_password(password)

    def change_tutor_biography(self, tutor_mail: str, biography: str) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            tutor.change_biography(biography)

    def change_tutor_profile_address(
        self, tutor_mail: str, profile_address: str
    ) -> None:
        tutor = self.get_tutor(tutor_mail)
        if tutor.email != "":
            tutor.change_profile_address(profile_address)

    def delete_tutor(self, tutor_mail: str) -> None:
        self.data.pop(tutor_mail)

    def get_tutors(
        self,
    ) -> List[Tutor]:
        return list(self.data.values())
