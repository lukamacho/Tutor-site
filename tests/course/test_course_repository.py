from app.infra.sqlite.course import SqlCourseRepository
from app.core.course.entity import Course

def test_create_course() -> None:
    course_repository = SqlCourseRepository("")

    subject = "Math"
    tutor_mail = "tutor@gmail.com"
    price = 50

    response = course_repository.create_course(subject, tutor_mail, price)

    assert isinstance(response, Course)
    assert response.subject is subject
    assert response.tutor_mail is tutor_mail
    assert response.price is price

def test_get_course() -> None:
    course_repository = SqlCourseRepository("")

    subject = "Physics"
    tutor_mail = "tutor@gmail.com"
    price = 50

    course_repository.create_course(subject, tutor_mail, price)
    get_response = course_repository.get_course(subject, tutor_mail)

    assert isinstance(get_response, Course)
    assert get_response.subject is subject
    assert get_response.tutor_mail is tutor_mail
    assert get_response.price is price

    subject = "Math"

    get_response = course_repository.get_tutor(subject, tutor_mail)

    assert get_response is None

def test_get_courses() -> None:
    course_repository = SqlCourseRepository("")

    subject_1 = "Chemistry"
    subject_2 = "Biology"
    num_subjects = 2
    tutor_mail = "tutor@gmail.com"
    price_1 = 50
    price_2 = 44

    course_repository.create_course(subject_1, tutor_mail, price_1)
    course_repository.create_course(subject_2, tutor_mail, price_2)
    get_response = course_repository.get_courses(tutor_mail)

    assert get_response.count() is num_subjects
    assert get_response[0].subject is subject_1
    assert get_response[1].subject is subject_2
    assert get_response[0].tutor_mail is tutor_mail
    assert get_response[1].tutor_mail is tutor_mail
    assert get_response[0].price is price_1
    assert get_response[1].price is price_2
