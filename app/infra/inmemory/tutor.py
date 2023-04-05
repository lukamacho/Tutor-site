from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Tutor:
    is_top_tutor = False
    first_name: str
    last_name: str
    languages: List[str]
    biography: str
    current_balance = 0
    commision_pct = 0.25
    subject_prices: Dict[str, int] = field(default_factory=dict)
    availability_calendar: Dict[str, int] = field(default_factory=dict)

    def set_tutor_info(self, first_name: str, last_name: str, biography: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.biography = biography

    def add_homework(self, student_id: int, homework_text: str) -> None:
        pass
