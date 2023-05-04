from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Tutor:
    first_name: str
    last_name: str
    email: str
    password: str
    commission_pct: float
    balance: 0
    biography: str
    languages: List[str] = field(default_factory=list)
    profile_address: str = ""
    is_top_tutor: bool = False
    subject_prices: Dict[str, int] = field(default_factory=dict)
    availability_calendar: Dict[str, int] = field(default_factory=dict)

    def set_tutor_info(self, first_name: str, last_name: str, biography: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.biography = biography

    def add_homework(self, student_id: int, homework_text: str) -> None:
        pass

    def add_language(self, language: str) -> None:
        self.languages.append(language)

    def set_balance(self, new_balance: int) -> None:
        self.balance = new_balance

    def get_balance(self) -> int:
        return self.balance

    def increase_balance(self, amount: int) -> None:
        self.balance += amount

    def decrease_balance(self, amount: int) -> None:
        self.balance -= amount

    def set_commission_pct(self, new_commission_pct: float) -> None:
        self.commission_pct = new_commission_pct

    def decrease_commission_pct(self) -> None:
        new_commission_pct = self.commission_pct - 0.01  # TODO: Save this value as const somewhere
        if new_commission_pct > 0:
            self.commission_pct = new_commission_pct
        else:
            self.commission_pct = 0  # TODO: Add some minimum limit

    def change_first_name(self, first_name: str) -> None:
        self.first_name = first_name

    def change_last_name(self, last_name: str) -> None:
        self.last_name = last_name

    def change_biography(self, biography: str) -> None:
        self.biography = biography
