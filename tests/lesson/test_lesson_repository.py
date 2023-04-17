from app.infra.sqlite.lesson import SqlLessonRepository
from app.core.lesson.entity import Lesson

def test_create_lesson() -> None:
    lesson_repository = SqlLessonRepository("")

    subject = "Math"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 5
    lesson_price = 30

    response = lesson_repository.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)

    assert isinstance(response, Lesson)
    assert response.subject is subject
    assert response.tutor_mail is tutor_mail
    assert response.student_mail is student_mail
    assert response.number_of_lessons is number_of_lessons
    assert lesson_price is lesson_price

def test_get_lesson() -> None:
    lesson_repository = SqlLessonRepository("")

    subject = "Chemistry"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 10
    lesson_price = 45

    lesson_repository.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    get_response = lesson_repository.get_lesson(tutor_mail, student_mail, subject)

    assert isinstance(get_response, Lesson)
    assert get_response.subject is subject
    assert get_response.tutor_mail is tutor_mail
    assert get_response.student_mail is student_mail
    assert get_response.number_of_lessons is number_of_lessons
    assert get_response.lesson_price is lesson_price

    new_subject = "Biology"
    new_tutor_mail = "tutor2@gmail.com"
    new_student_mail = "student2@gmail.com"

    get_response = lesson_repository.get_lesson(tutor_mail, student_mail, new_subject)
    assert get_response is None

    get_response = lesson_repository.get_lesson(new_tutor_mail, student_mail, subject)
    assert get_response is None

    get_response = lesson_repository.get_lesson(tutor_mail, new_student_mail, subject)
    assert get_response is None

def test_get_number_of_lessons() -> None:
    lesson_repository = SqlLessonRepository("")

    subject = "Astronomy"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 7
    lesson_price = 65

    lesson_repository.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    get_response = lesson_repository.get_number_of_lessons(tutor_mail, student_mail, subject)

    assert isinstance(get_response, int)
    assert get_response is number_of_lessons

def test_set_number_of_lessons() -> None:
    lesson_repository = SqlLessonRepository("")

    subject = "Ecology"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 13
    lesson_price = 35

    new_number_of_lessons = 7

    lesson_repository.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    lesson_repository.set_number_of_lessons(tutor_mail, student_mail, new_number_of_lessons, subject)
    get_response = lesson_repository.get_number_of_lessons(tutor_mail, student_mail, subject)

    assert isinstance(get_response, int)
    assert get_response is new_number_of_lessons

    new_number_of_lessons = 14

    lesson_repository.set_number_of_lessons(tutor_mail, student_mail, new_number_of_lessons, subject)
    get_response = lesson_repository.get_number_of_lessons(tutor_mail, student_mail, subject)

    assert isinstance(get_response, int)
    assert get_response is new_number_of_lessons

def test_change_number_of_lessons() -> None:
    lesson_repository = SqlLessonRepository("")

    subject = "Science"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 2
    lesson_price = 70

    increment = 2

    lesson_repository.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    lesson_repository.increase_lesson_number(tutor_mail, student_mail, increment, subject)
    get_response = lesson_repository.get_number_of_lessons(tutor_mail, student_mail, subject)

    new_number_of_lessons = number_of_lessons + increment

    assert isinstance(get_response, int)
    assert get_response is new_number_of_lessons

    decrement = 1

    lesson_repository.decrease_lesson_number(tutor_mail, student_mail, subject)
    get_response = lesson_repository.get_number_of_lessons(tutor_mail, student_mail, subject)

    assert isinstance(get_response, int)
    assert get_response is new_number_of_lessons - decrement

def test_set_lesson_price() -> None:
    lesson_repository = SqlLessonRepository("")

    subject = "Machine Learning"
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"
    number_of_lessons = 25
    lesson_price = 60

    new_lesson_price = 55

    lesson_repository.create_lesson(subject, tutor_mail, student_mail, number_of_lessons, lesson_price)
    lesson_repository.set_lesson_price(tutor_mail, student_mail, subject, new_lesson_price)
    get_response = lesson_repository.get_lesson(tutor_mail, student_mail, subject)

    assert isinstance(get_response.lesson_price, int)
    assert get_response.lesson_price is new_lesson_price

    new_lesson_price = 45

    lesson_repository.set_lesson_price(tutor_mail, student_mail, subject, new_lesson_price)
    get_response = lesson_repository.get_number_of_lessons(tutor_mail, student_mail, subject)

    assert isinstance(get_response.lesson_price, int)
    assert get_response.lesson_price is new_lesson_price
