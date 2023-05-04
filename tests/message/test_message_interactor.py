from app.core.message.entity import Message
from app.core.message.interactor import IMessageRepository, MessageInteractor


def test_create_message(message_repository: IMessageRepository) -> None:
    interactor = MessageInteractor(message_repository)

    message_text = "Hi!"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    response = interactor.create_message(message_text, tutor_mail, student_mail)

    assert isinstance(response, Message)
    assert message_repository.get_messages(tutor_mail, student_mail) is not None
    assert len(message_repository.get_messages("", student_mail)) == 0
    assert len(message_repository.get_messages(tutor_mail, "")) == 0


def test_create_messages(message_repository: IMessageRepository) -> None:
    interactor = MessageInteractor(message_repository)

    message_text = "Hi!"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    for i in range(10000):
        interactor.create_message(message_text, tutor_mail, student_mail)

    assert len(interactor.get_messages(tutor_mail, student_mail)) == 10000


def test_get_messages(message_repository: IMessageRepository) -> None:
    interactor = MessageInteractor(message_repository)

    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    interactor.create_message("Hey!", tutor_mail, student_mail)
    get_response = interactor.get_messages(tutor_mail, student_mail)

    assert len(get_response) == 1

    interactor.create_message("Hi!", tutor_mail, student_mail)
    get_response = interactor.get_messages(tutor_mail, student_mail)

    assert len(get_response) == 2

    get_response = interactor.get_messages("", student_mail)

    assert len(get_response) == 0


def test_delete_tutor_messages(message_repository: IMessageRepository) -> None:
    interactor = MessageInteractor(message_repository)

    tutor_mail = "tutor@gmail.com"
    student_mail_1 = "student1@gmail.com"
    student_mail_2 = "student2@gmail.com"

    interactor.create_message("A", tutor_mail, student_mail_1)
    interactor.create_message("B", tutor_mail, student_mail_1)
    interactor.create_message("C", tutor_mail, student_mail_1)
    interactor.create_message("D", tutor_mail, student_mail_1)
    interactor.create_message("E", tutor_mail, student_mail_2)
    interactor.create_message("F", tutor_mail, student_mail_2)

    get_response = interactor.get_messages(tutor_mail, student_mail_1)

    assert len(get_response) == 4

    get_response = interactor.get_messages(tutor_mail, student_mail_2)

    assert len(get_response) == 2

    interactor.delete_tutor_messages(tutor_mail)

    get_response = interactor.get_messages(tutor_mail, student_mail_1)

    assert len(get_response) == 0

    get_response = interactor.get_messages(tutor_mail, student_mail_2)

    assert len(get_response) == 0


def test_delete_student_messages(message_repository: IMessageRepository) -> None:
    interactor = MessageInteractor(message_repository)

    tutor_mail_1 = "tutor1@gmail.com"
    tutor_mail_2 = "tutor2@gmail.com"
    student_mail = "student@gmail.com"

    interactor.create_message("A", tutor_mail_1, student_mail)
    interactor.create_message("B", tutor_mail_1, student_mail)
    interactor.create_message("C", tutor_mail_1, student_mail)
    interactor.create_message("D", tutor_mail_1, student_mail)
    interactor.create_message("E", tutor_mail_2, student_mail)
    interactor.create_message("F", tutor_mail_2, student_mail)

    get_response = interactor.get_messages(tutor_mail_1, student_mail)

    assert len(get_response) == 4

    get_response = interactor.get_messages(tutor_mail_2, student_mail)

    assert len(get_response) == 2

    interactor.delete_student_messages(student_mail)

    get_response = interactor.get_messages(tutor_mail_1, student_mail)

    assert len(get_response) == 0

    get_response = interactor.get_messages(tutor_mail_2, student_mail)

    assert len(get_response) == 0
