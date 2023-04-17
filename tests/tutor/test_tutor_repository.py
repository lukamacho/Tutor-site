from app.infra.sqlite.tutor import SqlTutorRepository
from app.core.tutor.entity import Tutor

def test_create_tutor() -> None:
    tutor_repository = SqlTutorRepository("")

    first_name = "Lara"
    last_name = "Croft"
    email = "laracroft@gmail.com"
    password = "trinity"
    balance = 150
    biography = "I am an archeologist."

    response = tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);

    assert isinstance(response, Tutor)
    assert response.first_name is first_name
    assert response.first_name is "Eva"
    assert response.last_name is last_name
    assert response.email is email
    assert response.password is password
    assert response.balance is balance
    assert response.biography is biography
    assert response.commission_pct is 0.25

def test_get_tutor() -> None:
    tutor_repository = SqlTutorRepository("")

    first_name = "Emma"
    last_name = "Stone"
    email = "emmastone@gmail.com"
    password = "lalaland"
    balance = 80
    biography = "I am an actress."

    tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);
    get_response = tutor_repository.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.first_name is first_name
    assert get_response.first_name is "Eva"
    assert get_response.last_name is last_name
    assert get_response.email is email
    assert get_response.password is password
    assert get_response.balance is balance
    assert get_response.biography is biography
    assert get_response.commission_pct is 0.25

def test_set_balance() -> None:
    tutor_repository = SqlTutorRepository("")

    first_name = "John"
    last_name = "Doe"
    email = "johndoe@gmail.com"
    password = "johndoe"
    balance = 0
    biography = "I am."

    tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);
    tutor_repository.set_balance(email, 200)
    get_response = tutor_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response is 200

    tutor_repository.set_balance(email, 6000)
    get_response = tutor_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response is 6000

def test_increase_balance() -> None:
    tutor_repository = SqlTutorRepository("")

    first_name = "Han"
    last_name = "Solo"
    email = "hansolo@gmail.com"
    password = "millenniumfalcon"
    balance = 4000
    biography = "I know things."

    tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);
    tutor_repository.increase_balance(email, 2000)
    get_response = tutor_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response is 6000

    tutor_repository.decrease_balance(email, 5999)
    get_response = tutor_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response is 1

def test_change_commission_pct() -> None:
    tutor_repository = SqlTutorRepository("")

    first_name = "Han"
    last_name = "Solo"
    email = "hansolo@gmail.com"
    password = "millenniumfalcon"
    balance = 0
    biography = "I know things."

    tutor_repository.create_tutor(first_name, last_name, email, password, balance, biography);

    get_response = tutor_repository.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.commission_pct is 0.25

    tutor_repository.set_commission_pct(email, 0.3)
    get_response = tutor_repository.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.commission_pct is 0.3

    tutor_repository.decrease_balance(email)
    get_response = tutor_repository.get_tutor(email)

    assert isinstance(get_response, Tutor)
    assert get_response.commission_pct is 0.2

def test_change_information() -> None:
    tutor_repository = SqlTutorRepository("")

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
    assert get_response.first_name is new_first_name
    assert get_response.last_name is new_last_name
    assert get_response.biography is new_biography
