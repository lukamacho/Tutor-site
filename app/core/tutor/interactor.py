from typing import Protocol, Optional
from app.core.tutor.entity import Tutor
from dataclasses import dataclass


class ITutorInteractor(Protocol):
    def create_tutor(
        self, first_name: str, last_name: str, email: str, password: str, balance: int, biography: str
    ) -> Tutor:
        pass

    def get_tutor(self, email: str) -> Optional[Tutor]:
        pass

    def set_balance(self, tutor_mail: str, new_balance: int) -> None:
        pass

    def get_balance(self, tutor_mail: str) -> int:
        pass

    def increase_balance(self, tutor_mail: str, amount: int) -> None:
        pass

    def decrease_balance(self, tutor_mail: str, amount: int) -> None:
        pass

    def set_commission_pct(self, tutor_mail: str, new_commission_pct: float):
        pass

    def decrease_commission_pct(self, tutor_mail: str) -> None:
        pass

    def change_first_name(self, tutor_mail: str, first_name: str) -> None:
        pass

    def change_last_name(self, tutor_mail: str, last_name: str) -> None:
        pass

    def change_biography(self, tutor_mail: str, biography: str) -> None:
        pass


class ITutorRepository(Protocol):
    def create_tutor(
        self, first_name: str, last_name: str, email: str, password: str, balance: int, biography: str
    ) -> Tutor:
        pass

    def get_tutor(self, email: str) -> Optional[Tutor]:
        pass

    def set_tutor_balance(self, tutor_mail: str, new_balance: int) -> None:
        pass

    def get_tutor_balance(self, tutor_mail: str) -> int:
        pass

    def increase_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        pass

    def decrease_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        pass

    def set_commission_pct(self, tutor_mail: str, new_commission_pct: float):
        pass

    def decrease_commission_pct(self, tutor_mail: str) -> None:
        pass

    def change_tutor_first_name(self, tutor_mail: str, first_name: str) -> None:
        pass

    def change_tutor_last_name(self, tutor_mail: str, last_name: str) -> None:
        pass

    def change_tutor_biography(self, tutor_mail: str, biography: str) -> None:
        pass


@dataclass
class TutorInteractor:
    tutor_repository: ITutorRepository

    def create_tutor(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        balance: int,
        biography: str,
    ) -> Tutor:
        return self.tutor_repository.create_tutor(
            first_name, last_name, email, password, balance, biography
        )

    def get_tutor(self, email: str) -> Optional[Tutor]:
        return self.tutor_repository.get_tutor(email)

    def set_tutor_balance(self, tutor_mail: str, new_balance: int) -> None:
        self.tutor_repository.set_balance(tutor_mail, new_balance)

    def get_tutor_balance(self, tutor_mail: str) -> int:
        return self.tutor_repository.get_balance(tutor_mail)

    def increase_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        self.tutor_repository.increase_balance(tutor_mail, amount)

    def decrease_tutor_balance(self, tutor_mail: str, amount: int) -> None:
        self.tutor_repository.decrease_balance(tutor_mail, amount)

    def set_commission_pct(self, tutor_mail: str, new_commission_pct: float):
        self.tutor_repository.set_commission_pct(tutor_mail, new_commission_pct)

    def decrease_commission_pct(self, tutor_mail: str) -> None:
        self.tutor_repository.decrease_commission_pct(tutor_mail)

    def change_tutor_first_name(self, tutor_mail: str, first_name: str) -> None:
        self.tutor_repository.change_first_name(tutor_mail, first_name)

    def change_tutor_last_name(self, tutor_mail: str, last_name: str) -> None:
        self.tutor_repository.change_last_name(tutor_mail, last_name)

    def change_tutor_biography(self, tutor_mail: str, biography: str) -> None:
        self.tutor_repository.change_biography(tutor_mail, biography)
