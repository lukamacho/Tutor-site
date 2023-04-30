from app.core.tutor.interactor import ITutorRepository
from app.infra.sqlite.tutors import SqlTutorRepository
from app.core.tutor.entity import Tutor


def test_create_tutor(tutor_repository: ITutorRepository) -> None:
    first_name = "Lara"
    last_name = "Croft"
    email = "laracroft@gmail.com"
    password = "trinity"
    balance = 150
    biography = "I am an archeologist."

    response = tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography)

    assert isinstance(response, Tutor)
    assert response.first_name == first_name
    assert response.last_name == last_name
    assert response.email == email
    assert response.password == password
    assert response.balance == balance
    assert response.biography == biography
    assert response.commission_pct == 0.25


def test_get_tutor(tutor_repository: ITutorRepository) -> None:
    first_name = "Emma"
    last_name = "Stone"
    email = "emmastone@gmail.com"
    password = "lalaland"
    balance = 80
    biography = "I am an actress."

    tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);
    get_response = tutor_repository.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.first_name == first_name
    assert get_response.last_name == last_name
    assert get_response.email == email
    assert get_response.password == password
    assert get_response.balance == balance
    assert get_response.biography == biography
    assert get_response.commission_pct == 0.25

    new_email = "idontexist@gmail.com"

    get_response = tutor_repository.get_tutor(new_email)

    assert get_response is None


def test_set_balance(tutor_repository: ITutorRepository) -> None:
    first_name = "John"
    last_name = "Doe"
    email = "johndoe@gmail.com"
    password = "johndoe"
    balance = 0
    biography = "I am."

    new_balance = 200

    tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);
    tutor_repository.set_balance(email, new_balance)
    get_response = tutor_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance

    new_balance = 6000

    tutor_repository.set_balance(email, new_balance)
    get_response = tutor_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance


def test_change_balance(tutor_repository: ITutorRepository) -> None:
    first_name = "Han"
    last_name = "Solo"
    email = "hansolo@gmail.com"
    password = "millenniumfalcon"
    balance = 4000
    biography = "I know things."

    increment = 2000

    tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);
    tutor_repository.increase_balance(email, increment)
    get_response = tutor_repository.get_balance(email)

    new_balance = balance + increment

    assert isinstance(get_response, int)
    assert get_response == new_balance

    decrement = 5999

    tutor_repository.decrease_balance(email, decrement)
    get_response = tutor_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance - decrement


def test_change_commission_pct(tutor_repository: ITutorRepository) -> None:
    first_name = "Han"
    last_name = "Solo"
    email = "hansolo@gmail.com"
    password = "millenniumfalcon"
    balance = 0
    biography = "I know things."

    commission_pct = 0.25

    tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);

    get_response = tutor_repository.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.commission_pct == commission_pct

    new_commission_pct = 0.3

    tutor_repository.set_commission_pct(email, new_commission_pct)
    get_response = tutor_repository.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.commission_pct == new_commission_pct

    decrement = 0.01

    tutor_repository.decrease_commission_pct(email)
    get_response = tutor_repository.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.commission_pct == new_commission_pct - decrement


def test_change_information(tutor_repository: ITutorRepository) -> None:
    first_name = "John"
    last_name = "Doe"
    email = "johndoe@gmail.com"
    password = "johndoe"
    balance = 0
    biography = "I am."

    new_first_name = "Violet"
    new_last_name = "Dove"
    new_biography = "Who am I?"

    tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);
    tutor_repository.change_first_name(email, new_first_name)
    tutor_repository.change_last_name(email, new_last_name)
    tutor_repository.change_biography(email, new_biography)

    get_response = tutor_repository.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.first_name == new_first_name
    assert get_response.last_name == new_last_name
    assert get_response.biography == new_biography
