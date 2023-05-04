from app.core.message.entity import Message
from app.core.message.interactor import IMessageRepository


def test_create_message(message_repository: IMessageRepository) -> None:
    message_text = "Hi!"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    response = message_repository.create_message(message_text, tutor_mail, student_mail)

    assert isinstance(response, Message)
    assert response.message_text == message_text
    assert response.tutor_mail == tutor_mail
    assert response.student_mail == student_mail


def test_get_messages(message_repository: IMessageRepository) -> None:
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    message_repository.create_message("Hey!", tutor_mail, student_mail)
    get_response = message_repository.get_messages(tutor_mail, student_mail)

    assert len(get_response) == 1

    message_repository.create_message("Hi!", tutor_mail, student_mail)
    get_response = message_repository.get_messages(tutor_mail, student_mail)

    assert len(get_response) == 2

    get_response = message_repository.get_messages("", student_mail)

    assert len(get_response) == 0


def test_delete_tutor_messages(message_repository: IMessageRepository) -> None:
    tutor_mail = "tutor@gmail.com"
    student_mail_1 = "student1@gmail.com"
    student_mail_2 = "student2@gmail.com"

    message_repository.create_message("A", tutor_mail, student_mail_1)
    message_repository.create_message("B", tutor_mail, student_mail_1)
    message_repository.create_message("C", tutor_mail, student_mail_1)
    message_repository.create_message("D", tutor_mail, student_mail_1)
    message_repository.create_message("E", tutor_mail, student_mail_2)
    message_repository.create_message("F", tutor_mail, student_mail_2)

    get_response = message_repository.get_messages(tutor_mail, student_mail_1)

    assert len(get_response) == 4

    get_response = message_repository.get_messages(tutor_mail, student_mail_2)

    assert len(get_response) == 2

    message_repository.delete_tutor_messages(tutor_mail)

    get_response = message_repository.get_messages(tutor_mail, student_mail_1)

    assert len(get_response) == 0

    get_response = message_repository.get_messages(tutor_mail, student_mail_2)

    assert len(get_response) == 0


def test_delete_student_messages(message_repository: IMessageRepository) -> None:
    tutor_mail_1 = "tutor1@gmail.com"
    tutor_mail_2 = "tutor2@gmail.com"
    student_mail = "student@gmail.com"

    message_repository.create_message("A", tutor_mail_1, student_mail)
    message_repository.create_message("B", tutor_mail_1, student_mail)
    message_repository.create_message("C", tutor_mail_1, student_mail)
    message_repository.create_message("D", tutor_mail_1, student_mail)
    message_repository.create_message("E", tutor_mail_2, student_mail)
    message_repository.create_message("F", tutor_mail_2, student_mail)

    get_response = message_repository.get_messages(tutor_mail_1, student_mail)

    assert len(get_response) == 4

    get_response = message_repository.get_messages(tutor_mail_2, student_mail)

    assert len(get_response) == 2

    message_repository.delete_student_messages(student_mail)

    get_response = message_repository.get_messages(tutor_mail_1, student_mail)

    assert len(get_response) == 0

    get_response = message_repository.get_messages(tutor_mail_2, student_mail)

    assert len(get_response) == 0
