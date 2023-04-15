from dataclasses import dataclass
from typing import List


@dataclass
class Tutor:
    first_name: str
    last_name: str
    email: str
    commision_pct: int
    balance: int
    biography: str
    language: List[str]
