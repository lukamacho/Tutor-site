from app.core.lesson.entity import Lesson
from app.core.lesson.interactor import ILessonRepository, LessonInteractor


def test_create_lesson(lesson_repository: ILessonRepository) -> None:
    interactor = LessonInteractor(lesson_repository)

    subject = "Math"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    response = interactor.create_lesson(subject, tutor_mail, student_mail, 5, 70)

    assert isinstance(response, Lesson)
    assert interactor.get_lesson(tutor_mail, student_mail, subject) is not None
    assert interactor.get_lesson(tutor_mail, "", subject) is None
    assert interactor.get_lesson(tutor_mail, student_mail, "") is None


def test_get_lesson(lesson_repository: ILessonRepository) -> None:
    interactor = LessonInteractor(lesson_repository)

    subject = "Chemistry"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 10
    lesson_price = 45

    interactor.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    get_response = interactor.get_lesson(tutor_mail, student_mail, subject)

    assert isinstance(get_response, Lesson)
    assert get_response.subject == subject
    assert get_response.tutor_mail == tutor_mail
    assert get_response.student_mail == student_mail
    assert get_response.number_of_lessons == number_of_lessons
    assert get_response.lesson_price == lesson_price

    new_subject = "Biology"
    new_tutor_mail = "tutor2@gmail.com"
    new_student_mail = "student2@gmail.com"

    get_response = interactor.get_lesson(tutor_mail, student_mail, new_subject)
    assert get_response is None

    get_response = interactor.get_lesson(new_tutor_mail, student_mail, subject)
    assert get_response is None

    get_response = interactor.get_lesson(tutor_mail, new_student_mail, subject)
    assert get_response is None


def test_get_number_of_lessons(lesson_repository: ILessonRepository) -> None:
    interactor = LessonInteractor(lesson_repository)

    subject = "Astronomy"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 7
    lesson_price = 65

    interactor.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    get_response = interactor.get_number_of_lessons(tutor_mail, student_mail, subject)

    assert isinstance(get_response, int)
    assert get_response == number_of_lessons


def test_set_number_of_lessons(lesson_repository: ILessonRepository) -> None:
    interactor = LessonInteractor(lesson_repository)

    subject = "Ecology"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 13
    lesson_price = 35

    new_number_of_lessons = 7

    interactor.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    interactor.set_number_of_lessons(tutor_mail, student_mail, new_number_of_lessons, subject)
    get_response = interactor.get_number_of_lessons(tutor_mail, student_mail, subject)

    assert isinstance(get_response, int)
    assert get_response == new_number_of_lessons

    new_number_of_lessons = 14

    interactor.set_number_of_lessons(tutor_mail, student_mail, new_number_of_lessons, subject)
    get_response = interactor.get_number_of_lessons(tutor_mail, student_mail, subject)

    assert isinstance(get_response, int)
    assert get_response == new_number_of_lessons


def test_change_number_of_lessons(lesson_repository: ILessonRepository) -> None:
    interactor = LessonInteractor(lesson_repository)

    subject = "Science"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 2
    lesson_price = 70

    increment = 2

    interactor.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    interactor.increase_lesson_number(tutor_mail, student_mail, increment, subject)
    get_response = interactor.get_number_of_lessons(tutor_mail, student_mail, subject)

    new_number_of_lessons = number_of_lessons + increment

    assert isinstance(get_response, int)
    assert get_response == new_number_of_lessons

    decrement = 1

    interactor.decrease_lesson_number(tutor_mail, student_mail, subject)
    get_response = interactor.get_number_of_lessons(tutor_mail, student_mail, subject)

    assert isinstance(get_response, int)
    assert get_response == new_number_of_lessons - decrement


def test_set_lesson_price(lesson_repository: ILessonRepository) -> None:
    interactor = LessonInteractor(lesson_repository)

    subject = "Machine Learning"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 25
    lesson_price = 60

    new_lesson_price = 55

    interactor.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    interactor.set_lesson_price(tutor_mail, student_mail, subject, new_lesson_price)
    get_response = interactor.get_lesson(tutor_mail, student_mail, subject)

    assert isinstance(get_response.lesson_price, int)
    assert get_response.lesson_price == new_lesson_price

    new_lesson_price = 45

    interactor.set_lesson_price(tutor_mail, student_mail, subject, new_lesson_price)
    get_response = interactor.get_lesson(tutor_mail, student_mail, subject)

    assert isinstance(get_response, Lesson)
    assert get_response.lesson_price == new_lesson_price
