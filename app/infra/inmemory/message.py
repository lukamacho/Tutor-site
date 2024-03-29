from dataclasses import dataclass, field
from typing import List

from app.core.message.entity import Message


@dataclass
class InMemoryMessageRepository:
    data: List[Message] = field(default_factory=list)

    def create_message(
        self, message_text: str, tutor_mail: str, student_mail: str
    ) -> Message:
        message = Message(message_text, tutor_mail, student_mail)
        self.data.append(message)
        return message

    def get_messages(self, tutor_mail: str, student_mail: str) -> List[Message]:
        messages: List[Message] = []
        for message in self.data:
            if (
                message.tutor_mail == tutor_mail
                and message.student_mail == student_mail
            ):
                messages.append(message)
        return messages

    def get_tutor_student_messages(self, tutor_mail: str) -> List[str]:
        tutor_students: List[str] = []
        for message in self.data:
            if message.tutor_mail == tutor_mail:
                tutor_students.append(message.student_mail)

        return tutor_students

    def get_student_tutor_messages(self, student_mail: str) -> List[str]:
        student_tutors: List[str] = []
        for message in self.data:
            if message.student_mail == student_mail:
                student_tutors.append(message.tutor_mail)
        return student_tutors

    def delete_tutor_messages(self, tutor_mail: str) -> None:
        i = 0
        length = len(self.data)

        while i < length:
            message = self.data[i]
            if message.tutor_mail == tutor_mail:
                self.data.remove(message)
                i -= 1
                length -= 1
            i += 1

    def delete_student_messages(self, student_mail: str) -> None:
        i = 0
        length = len(self.data)

        while i < length:
            message = self.data[i]
            if message.student_mail == student_mail:
                self.data.remove(message)
                i -= 1
                length -= 1
            i += 1

    def get_student_messaged_tutors(self, student_mail: str) -> list[str]:
        return []

    def get_tutor_messaged_students(self, tutor_mail: str) -> list[str]:
        return []
