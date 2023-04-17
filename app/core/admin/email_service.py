import smtplib
import ssl


def send_mail(receiver_email: str, message: str) -> None:
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "tutorsite727@gmail.com"
    password = "fvqxtupjruxqcooo"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
