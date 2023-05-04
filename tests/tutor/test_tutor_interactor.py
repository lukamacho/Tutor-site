from app.core.tutor.entity import Tutor
from app.core.tutor.interactor import ITutorRepository, TutorInteractor


def test_create_tutor(tutor_repository: ITutorRepository) -> None:
    interactor = TutorInteractor(tutor_repository)

    mail = "johndoe@gmail.com"

    response = interactor.create_tutor("John", "Doe", mail, "johndoe", 0, "I'm John.")

    assert isinstance(response, Tutor)
    assert tutor_repository.get_tutor(mail) is not None
    assert tutor_repository.get_tutor("") is None


def test_create_tutors(tutor_repository: ITutorRepository) -> None:
    interactor = TutorInteractor(tutor_repository)

    for i in range(10000):
        mail = "johndoe{i}@gmail.com".format(i=i)
        response = interactor.create_tutor("John", "Doe", mail, "johndoe", 0, "I'm John.")
        assert isinstance(response, Tutor)
        assert tutor_repository.get_tutor(mail) is not None


def test_get_tutor(tutor_repository: ITutorRepository) -> None:
    interactor = TutorInteractor(tutor_repository)

    first_name = "Emma"
    last_name = "Stone"
    email = "emmastone@gmail.com"
    password = "lalaland"
    balance = 80
    biography = "I am an actress."

    interactor.create_tutor(first_name, last_name, email, password, balance, biography)
    get_response = interactor.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.first_name == first_name
    assert get_response.last_name == last_name
    assert get_response.email == email
    assert get_response.password == password
    assert get_response.balance == balance
    assert get_response.biography == biography
    assert get_response.commission_pct == 0.25

    new_email = "idontexist@gmail.com"

    get_response = interactor.get_tutor(new_email)

    assert get_response is None


def test_set_balance(tutor_repository: ITutorRepository) -> None:
    interactor = TutorInteractor(tutor_repository)

    first_name = "John"
    last_name = "Doe"
    email = "johndoe@gmail.com"
    password = "johndoe"
    balance = 0
    biography = "I am."

    new_balance = 200

    interactor.create_tutor(first_name, last_name, email, password, balance, biography)
    interactor.set_tutor_balance(email, new_balance)
    get_response = interactor.get_tutor_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance

    new_balance = 6000

    interactor.set_tutor_balance(email, new_balance)
    get_response = interactor.get_tutor_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance


def test_change_balance(tutor_repository: ITutorRepository) -> None:
    interactor = TutorInteractor(tutor_repository)

    first_name = "Han"
    last_name = "Solo"
    email = "hansolo@gmail.com"
    password = "millenniumfalcon"
    balance = 4000
    biography = "I know things."

    increment = 2000

    interactor.create_tutor(first_name, last_name, email, password, balance, biography)
    interactor.increase_tutor_balance(email, increment)
    get_response = interactor.get_tutor_balance(email)

    new_balance = balance + increment

    assert isinstance(get_response, int)
    assert get_response == new_balance

    decrement = 5999

    interactor.decrease_tutor_balance(email, decrement)
    get_response = interactor.get_tutor_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance - decrement


def test_change_commission_pct(tutor_repository: ITutorRepository) -> None:
    interactor = TutorInteractor(tutor_repository)

    first_name = "Han"
    last_name = "Solo"
    email = "hansolo@gmail.com"
    password = "millenniumfalcon"
    balance = 0
    biography = "I know things."

    commission_pct = 0.25

    interactor.create_tutor(first_name, last_name, email, password, balance, biography)

    get_response = interactor.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.commission_pct == commission_pct

    new_commission_pct = 0.3

    interactor.set_commission_pct(email, new_commission_pct)
    get_response = interactor.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.commission_pct == new_commission_pct

    decrement = 0.01

    interactor.decrease_commission_pct(email)
    get_response = interactor.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.commission_pct == new_commission_pct - decrement


def test_change_information(tutor_repository: ITutorRepository) -> None:
    interactor = TutorInteractor(tutor_repository)

    first_name = "John"
    last_name = "Doe"
    email = "johndoe@gmail.com"
    password = "johndoe"
    balance = 0
    biography = "I am."

    new_first_name = "Violet"
    new_last_name = "Dove"
    new_biography = "Who am I?"

    interactor.create_tutor(first_name, last_name, email, password, balance, biography)
    interactor.change_tutor_first_name(email, new_first_name)
    interactor.change_tutor_last_name(email, new_last_name)
    interactor.change_tutor_biography(email, new_biography)

    get_response = interactor.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.first_name == new_first_name
    assert get_response.last_name == new_last_name
    assert get_response.biography == new_biography
