from app.core.review.entity import Review
from app.core.review.interactor import IReviewRepository, ReviewInteractor


def test_create_review(review_repository: IReviewRepository) -> None:
    interactor = ReviewInteractor(review_repository)

    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    response = interactor.create_review("Great tutor.", tutor_mail, student_mail)

    assert isinstance(response, Review)
    assert review_repository.get_review(tutor_mail, student_mail) is not None
    assert review_repository.get_review("", student_mail) is None
    assert review_repository.get_review(tutor_mail, "") is None


def test_create_reviews(review_repository: IReviewRepository) -> None:
    interactor = ReviewInteractor(review_repository)

    tutor_mail = "tutor@gmail.com"

    for i in range(10000):
        student_mail = "student{i}@gmail.com".format(i=i)
        interactor.create_review("Good tutor.", tutor_mail, student_mail)

    assert len(interactor.get_tutor_reviews(tutor_mail)) == 10000


def test_get_review(review_repository: IReviewRepository) -> None:
    interactor = ReviewInteractor(review_repository)

    review_text = "Great tutor."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    interactor.create_review(review_text, tutor_mail, student_mail)
    get_response = interactor.get_review(tutor_mail, student_mail)

    assert isinstance(get_response, Review)
    assert get_response.review_text == review_text
    assert get_response.tutor_mail == tutor_mail
    assert get_response.student_mail == student_mail

    new_student_mail = "student2@gmail.com"

    get_response = interactor.get_review(tutor_mail, new_student_mail)

    assert get_response is None


def test_delete_review(review_repository: IReviewRepository) -> None:
    interactor = ReviewInteractor(review_repository)

    review_text = "Great tutor."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    interactor.create_review(review_text, tutor_mail, student_mail)
    get_response = interactor.get_review(tutor_mail, student_mail)

    assert get_response is not None

    interactor.delete_review(tutor_mail, student_mail)
    get_response = interactor.get_review(tutor_mail, student_mail)

    assert get_response is None


def test_change_review(review_repository: IReviewRepository) -> None:
    interactor = ReviewInteractor(review_repository)

    review_text = "Great tutor."
    tutor_mail = "tutor@gmail.com"
    student_mail = "student@gmail.com"

    interactor.create_review(review_text, tutor_mail, student_mail)
    get_response = interactor.get_review(tutor_mail, student_mail)

    assert isinstance(get_response, Review)
    assert get_response.review_text == review_text

    new_review_text = "Very great tutor."

    interactor.change_review(new_review_text, tutor_mail, student_mail)
    get_response = interactor.get_review(tutor_mail, student_mail)

    assert isinstance(get_response, Review)
    assert get_response.review_text == new_review_text
