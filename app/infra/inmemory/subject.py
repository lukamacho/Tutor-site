from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Subject:
    title: str
    description: str

    def set_subject_info(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
