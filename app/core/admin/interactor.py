import smtplib
import ssl
from dataclasses import dataclass
from typing import Protocol


class IEmailService(Protocol):
    def send_mail(self,receiver_email: str, message: str) -> None:
        pass


@dataclass
class AdminInteractor:
    email_service : IEmailService
    def send_hello(self,):
        self.email_service.send_mail("skhokhi@gmail.com", "hello")


