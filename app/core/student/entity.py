from dataclasses import dataclass


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    balance: int
