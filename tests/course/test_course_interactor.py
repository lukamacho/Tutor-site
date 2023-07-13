from app.core.course.entity import Course
from app.core.course.interactor import CourseInteractor, ICourseRepository


def test_create_course(course_repository: ICourseRepository) -> None:
    interactor = CourseInteractor(course_repository)

    subject = "Math"
    mail = "johndoe@gmail.com"

    response = interactor.create_course(subject, mail, 60)

    assert isinstance(response, Course)
    assert course_repository.get_course(subject, mail) is not None
    assert course_repository.get_course(subject, "").subject == ""
    assert course_repository.get_course("", mail).tutor_mail == ""


def test_create_courses(course_repository: ICourseRepository) -> None:
    interactor = CourseInteractor(course_repository)

    subject = "Math"

    for i in range(10000):
        mail = "johndoe{i}@gmail.com".format(i=i)
        response = interactor.create_course(subject, mail, 35)
        assert isinstance(response, Course)
        assert course_repository.get_course(subject, mail) is not None
        assert course_repository.get_courses() is not None


def test_get_course(course_repository: ICourseRepository) -> None:
    interactor = CourseInteractor(course_repository)

    subject = "Physics"
    tutor_mail = "tutor@gmail.com"
    price = 50

    interactor.create_course(subject, tutor_mail, price)
    get_response = interactor.get_course(subject, tutor_mail)

    assert isinstance(get_response, Course)
    assert get_response.subject == subject
    assert get_response.tutor_mail == tutor_mail
    assert get_response.price == price

    subject = "Math"

    get_response = interactor.get_course(subject, tutor_mail)

    assert get_response.tutor_mail == ""


def test_get_courses(course_repository: ICourseRepository) -> None:
    interactor = CourseInteractor(course_repository)

    subject_1 = "Chemistry"
    subject_2 = "Biology"
    num_subjects = 2
    tutor_mail = "tutor@gmail.com"
    price_1 = 50
    price_2 = 44

    interactor.create_course(subject_1, tutor_mail, price_1)
    interactor.create_course(subject_2, tutor_mail, price_2)
    get_response = interactor.get_tutor_courses(tutor_mail)

    assert len(get_response) == num_subjects
    assert get_response[0].subject == subject_1
    assert get_response[1].subject == subject_2
    assert get_response[0].tutor_mail == tutor_mail
    assert get_response[1].tutor_mail == tutor_mail
    assert get_response[0].price == price_1
    assert get_response[1].price == price_2


def test_delete_course(course_repository: ICourseRepository) -> None:
    interactor = CourseInteractor(course_repository)

    subject_1 = "Chemistry"
    subject_2 = "Biology"
    num_subjects = 2
    tutor_mail = "tutor@gmail.com"
    price_1 = 50
    price_2 = 44

    interactor.create_course(subject_1, tutor_mail, price_1)
    interactor.create_course(subject_2, tutor_mail, price_2)
    get_response = course_repository.get_tutor_courses(tutor_mail)

    assert len(get_response) == num_subjects
    interactor.delete_course(tutor_mail, subject_1)
    get_response = interactor.get_tutor_courses(tutor_mail)
    assert len(get_response) == (num_subjects - 1)
