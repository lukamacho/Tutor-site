from app.core.review.interactor import IReviewRepository
from app.infra.sqlite.review import SqlReviewRepository
from app.core.review.entity import Review


def test_create_review(review_repository: IReviewRepository) -> None:
    review_text = "Great tutor."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    response = review_repository.create_review(review_text, tutor_mail, student_mail)

    assert isinstance(response, Review)
    assert response.review_text == review_text
    assert response.tutor_mail == tutor_mail
    assert response.student_mail == student_mail


def test_get_review(review_repository: IReviewRepository) -> None:
    review_text = "Great tutor."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    review_repository.create_review(review_text, tutor_mail, student_mail)
    get_response = review_repository.get_review(tutor_mail, student_mail)

    assert isinstance(get_response, Review)
    assert get_response.review_text == review_text
    assert get_response.tutor_mail == tutor_mail
    assert get_response.student_mail == student_mail

    new_student_mail = "student2@gmail.com"

    get_response = review_repository.get_review(tutor_mail, new_student_mail)

    assert get_response is None


def test_delete_review(review_repository: IReviewRepository) -> None:
    review_text = "Great tutor."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    review_repository.create_review(review_text, tutor_mail, student_mail)
    get_response = review_repository.get_review(tutor_mail, student_mail)

    assert get_response is not None

    review_repository.delete_review(tutor_mail, student_mail)
    get_response = review_repository.get_review(tutor_mail, student_mail)

    assert get_response is None


def test_change_review(review_repository: IReviewRepository) -> None:
    review_text = "Great tutor."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    review_repository.create_review(review_text, tutor_mail, student_mail)
    get_response = review_repository.get_review(tutor_mail, student_mail)

    assert isinstance(get_response, Review)
    assert get_response.review_text == review_text

    new_review_text = "Very great tutor."

    review_repository.change_review(new_review_text, tutor_mail, student_mail)
    get_response = review_repository.get_review(tutor_mail, student_mail)

    assert isinstance(get_response, Review)
    assert get_response.review_text == new_review_text
