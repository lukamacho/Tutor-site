from dataclasses import dataclass
from typing import List, Protocol

from app.core.message.entity import Message


class IMessageInteractor(Protocol):
    def create_message(
        self, message_text: str, tutor_mail: str, student_mail: str
    ) -> Message:
        pass

    def get_messages(self, tutor_mail: str, student_mail: str) -> List[Message]:
        pass

    def delete_tutor_messages(self, tutor_mail: str) -> None:
        pass

    def delete_student_messages(self, student_mail: str) -> None:
        pass

    def get_student_messaged_tutors(self, student_mail: str) -> List[str]:
        pass

    def get_tutor_messaged_students(self, tutor_mail: str) -> List[str]:
        pass


class IMessageRepository(Protocol):
    def create_message(
        self, message_text: str, tutor_mail: str, student_mail: str
    ) -> Message:
        pass

    def get_messages(self, tutor_mail: str, student_mail: str) -> List[Message]:
        pass

    def delete_tutor_messages(self, tutor_mail: str) -> None:
        pass

    def delete_student_messages(self, student_mail: str) -> None:
        pass

    def get_student_messaged_tutors(self, student_mail: str) -> List[str]:
        pass

    def get_tutor_messaged_students(self, tutor_mail: str) -> List[str]:
        pass


@dataclass
class MessageInteractor:
    message_repository: IMessageRepository

    def create_message(
        self, message_text: str, tutor_mail: str, student_mail: str
    ) -> Message:
        return self.message_repository.create_message(
            message_text, tutor_mail, student_mail
        )

    def get_messages(self, tutor_mail: str, student_mail: str) -> List[Message]:
        return self.message_repository.get_messages(tutor_mail, student_mail)

    def delete_tutor_messages(self, tutor_mail: str) -> None:
        self.message_repository.delete_tutor_messages(tutor_mail)

    def delete_student_messages(self, student_mail: str) -> None:
        self.message_repository.delete_student_messages(student_mail)

    def get_student_messaged_tutors(self, student_mail: str) -> List[str]:
        return self.message_repository.get_student_messaged_tutors(student_mail)

    def get_tutor_messaged_students(self, tutor_mail: str) -> List[str]:
        return self.message_repository.get_tutor_messaged_students(tutor_mail)
