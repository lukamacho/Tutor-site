from app.core.course.entity import Course
from app.core.course.interactor import ICourseRepository


def test_create_course(course_repository: ICourseRepository) -> None:
    subject = "Math"
    tutor_mail = "tutor@gmail.com"
    price = 50

    response = course_repository.create_course(subject, tutor_mail, price)

    assert isinstance(response, Course)
    assert response.subject is subject
    assert response.tutor_mail is tutor_mail
    assert response.price is price


def test_get_course(course_repository: ICourseRepository) -> None:
    subject = "Physics"
    tutor_mail = "tutor@gmail.com"
    price = 50

    course_repository.create_course(subject, tutor_mail, price)
    get_response = course_repository.get_course(subject, tutor_mail)

    assert isinstance(get_response, Course)
    assert get_response.subject == subject
    assert get_response.tutor_mail == tutor_mail
    assert get_response.price == price

    subject = "Math"

    get_response = course_repository.get_course(subject, tutor_mail)

    assert get_response.tutor_mail == ""
    assert get_response.subject == ""
    assert get_response.price == 0


def test_get_courses(course_repository: ICourseRepository) -> None:
    subject_1 = "Chemistry"
    subject_2 = "Biology"
    num_subjects = 2
    tutor_mail = "tutor@gmail.com"
    price_1 = 50
    price_2 = 44

    course_repository.create_course(subject_1, tutor_mail, price_1)
    course_repository.create_course(subject_2, tutor_mail, price_2)
    get_response = course_repository.get_tutor_courses(tutor_mail)

    assert len(get_response) == num_subjects
    assert get_response[0].subject == subject_1
    assert get_response[1].subject == subject_2
    assert get_response[0].tutor_mail == tutor_mail
    assert get_response[1].tutor_mail == tutor_mail
    assert get_response[0].price == price_1
    assert get_response[1].price == price_2


def test_delete_course(course_repository: ICourseRepository) -> None:
    subject_1 = "Chemistry"
    subject_2 = "Biology"
    num_subjects = 2
    tutor_mail = "tutor@gmail.com"
    price_1 = 50
    price_2 = 44

    course_repository.create_course(subject_1, tutor_mail, price_1)
    course_repository.create_course(subject_2, tutor_mail, price_2)
    get_response = course_repository.get_tutor_courses(tutor_mail)

    assert len(get_response) == num_subjects
    course_repository.delete_course(tutor_mail, subject_1)
    get_response = course_repository.get_tutor_courses(tutor_mail)
    assert len(get_response) == (num_subjects - 1)
