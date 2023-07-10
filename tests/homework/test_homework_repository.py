from app.core.homework.entity import Homework
from app.core.homework.interactor import IHomeworkRepository


def test_create_homework(homework_repository: IHomeworkRepository) -> None:
    homework_text = "Solve three problems."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    response = homework_repository.create_homework(
        homework_text, tutor_mail, student_mail
    )

    assert isinstance(response, Homework)
    assert response.homework_text == homework_text
    assert response.tutor_mail == tutor_mail
    assert response.student_mail == student_mail


def test_change_homework(homework_repository: IHomeworkRepository) -> None:
    homework_text = "Solve three problems."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    new_homework_text = "Solve five problems."

    homework_repository.create_homework(homework_text, tutor_mail, student_mail)
    homework_repository.change_homework(
        new_homework_text, homework_text, tutor_mail, student_mail
    )
    response = homework_repository.get_student_homework(student_mail)

    assert response is not None


def test_get_student_homework(homework_repository: IHomeworkRepository) -> None:
    homework_text = "Solve three problems."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    new_student_mail = "someone@gmail.com"

    homework_repository.create_homework(homework_text, tutor_mail, student_mail)
    response = homework_repository.get_student_homework(student_mail)

    assert response is not None

    response = homework_repository.get_student_homework(new_student_mail)

    assert len(response) == 0


def test_delete_homework(homework_repository: IHomeworkRepository) -> None:
    homework_text = "Solve three problems."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    homework_repository.create_homework(homework_text, tutor_mail, student_mail)
    homework_repository.delete_homework(homework_text, tutor_mail, student_mail)
    response = homework_repository.get_student_homework(student_mail)

    assert len(response) == 0
