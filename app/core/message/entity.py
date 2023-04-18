from dataclasses import dataclass


@dataclass
class Message:
    message_text: str
    tutor_mail: str
    student_mail: str
