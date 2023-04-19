from dataclasses import dataclass
from typing import Protocol


class IEmailService(Protocol):
    def send_mail(self, receiver_email: str, message: str) -> None:
        pass


@dataclass
class AdminInteractor:
    email_service: IEmailService

    def send_hello(
        self,
    ) -> None:
        self.email_service.send_mail(self,"lmach19@freeuni.edu.ge", "hello")
