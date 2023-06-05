import smtplib
import ssl
from random import choices
from string import ascii_letters, digits


def generate_new_password() -> str:
    # Generate a random password
    password_length = 8
    characters = ascii_letters + digits
    new_password = "".join(choices(characters, k=password_length))
    return new_password


class SMTPEmailService:
    def send_mail(self, receiver_email: str, message: str) -> None:
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "tutorsite727@gmail.com"
        password = "fvqxtupjruxqcooo"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

    def send_verification(self, receiver_mail: str, random_int: str) -> int:
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "tutorsite727@gmail.com"
        password = "fvqxtupjruxqcooo"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_mail, random_int)

    def send_new_password(self, receiver_mail: str) -> str:
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "tutorsite727@gmail.com"
        password = "fvqxtupjruxqcooo"

        context = ssl.create_default_context()
        new_password = generate_new_password()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_mail, new_password)
