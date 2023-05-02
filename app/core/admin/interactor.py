import random
from dataclasses import dataclass
from typing import Protocol


class IEmailService(Protocol):
    def send_mail(self, receiver_email: str, message: str) -> None:
        pass

    def send_verification(self, receiver_mail: str, random_int: int) -> int:
        pass


@dataclass
class AdminInteractor:
    email_service: IEmailService

    def send_hello(
        self,
    ) -> None:
        self.email_service.send_mail(self, "lmach19@freeuni.edu.ge", "hello")

    def send_verification(self) -> None:
        random_integer = str(random.randint(1, 10000000))
        self.email_service.send_verification(
            self, "lmach19@freeuni.edu.ge", random_integer
        )
