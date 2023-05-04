from app.core.homework.entity import Homework
from app.core.homework.interactor import HomeworkInteractor, IHomeworkRepository


def test_create_homework(homework_repository: IHomeworkRepository) -> None:
    interactor = HomeworkInteractor(homework_repository)

    student_mail = "student@gmail.com"

    response = interactor.create_homework("Solve one problem.", "tutor@gmail.com", student_mail)

    assert isinstance(response, Homework)
    assert homework_repository.get_student_homework(student_mail) is not None
    assert len(homework_repository.get_student_homework("")) == 0


def test_create_homeworks(homework_repository: IHomeworkRepository) -> None:
    interactor = HomeworkInteractor(homework_repository)

    student_mail = "student@gmail.com"

    for i in range(10000):
        homework = "Solve #{i}".format(i=i)
        response = interactor.create_homework(homework, "tutor@gmail.com", student_mail)
        assert isinstance(response, Homework)

    assert len(homework_repository.get_student_homework(student_mail)) == 10000


def test_create_homework(homework_repository: IHomeworkRepository) -> None:
    interactor = HomeworkInteractor(homework_repository)

    homework_text = "Solve three problems."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    response = interactor.create_homework(homework_text, tutor_mail, student_mail)

    assert isinstance(response, Homework)
    assert response.homework_text == homework_text
    assert response.tutor_mail == tutor_mail
    assert response.student_mail == student_mail


def test_change_homework(homework_repository: IHomeworkRepository) -> None:
    interactor = HomeworkInteractor(homework_repository)

    homework_text = "Solve three problems."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    new_homework_text = "Solve five problems."

    interactor.create_homework(homework_text, tutor_mail, student_mail)
    interactor.change_homework(new_homework_text, homework_text, tutor_mail, student_mail)
    response = interactor.get_student_homework(student_mail)

    assert response is not None


def test_get_student_homework(homework_repository: IHomeworkRepository) -> None:
    interactor = HomeworkInteractor(homework_repository)

    homework_text = "Solve three problems."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    new_student_mail = "someone@gmail.com"

    interactor.create_homework(homework_text, tutor_mail, student_mail)
    response = interactor.get_student_homework(student_mail)

    assert response is not None

    response = interactor.get_student_homework(new_student_mail)

    assert len(response) == 0


def test_delete_homework(homework_repository: IHomeworkRepository) -> None:
    interactor = HomeworkInteractor(homework_repository)

    homework_text = "Solve three problems."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    interactor.create_homework(homework_text, tutor_mail, student_mail)
    interactor.delete_homework(homework_text, tutor_mail, student_mail)
    response = interactor.get_student_homework(student_mail)

    assert len(response) == 0
