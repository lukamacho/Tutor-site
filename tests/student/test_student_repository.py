from app.infra.sqlite.student import SqlStudentRepository
from app.core.student.entity import Student


def test_create_student() -> None:
    student_repository = SqlStudentRepository("")

    first_name = "Anne"
    last_name = "Warwick"
    email = "annewarwick@gmail.com"
    password = "anne123"
    balance = 0

    response = student_repository.create_student(first_name, last_name, email, password, balance)

    assert isinstance(response, Student)
    assert response.first_name == first_name
    assert response.last_name == last_name
    assert response.email == email
    assert response.password == password
    assert response.balance == balance


def test_get_student() -> None:
    student_repository = SqlStudentRepository("")

    first_name = "Mia"
    last_name = "Seaworth"
    email = "miaseaworth@gmail.com"
    password = "mia123"
    balance = 100

    student_repository.create_student(first_name, last_name, email, password, balance)
    get_response = student_repository.get_student(email)

    assert isinstance(get_response, Student)
    assert get_response.first_name == first_name
    assert get_response.last_name == last_name
    assert get_response.email == email
    assert get_response.password == password
    assert get_response.balance == balance

    new_email = "idontexist@gmail.com"

    get_response = student_repository.get_student(new_email)

    assert get_response is None


def test_set_balance() -> None:
    student_repository = SqlStudentRepository("")

    first_name = "Nina"
    last_name = "Fanning"
    email = "ninafanning@gmail.com"
    password = "nina123"
    balance = 50

    new_balance = 100

    student_repository.create_student(first_name, last_name, email, password, balance)
    student_repository.set_balance(email, new_balance)
    get_response = student_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance

    new_balance = 150

    student_repository.set_balance(email, new_balance)
    get_response = student_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance


def test_change_balance() -> None:
    student_repository = SqlStudentRepository("")

    first_name = "Emma"
    last_name = "Murdoch"
    email = "emmamurdoch@gmail.com"
    password = "emma123"
    balance = 0

    increment = 60

    student_repository.create_student(first_name, last_name, email, password, balance)
    student_repository.increase_balance(email, increment)
    get_response = student_repository.get_balance(email)

    new_balance = balance + increment

    assert isinstance(get_response, int)
    assert get_response == new_balance

    decrement = 50

    student_repository.decrease_balance(email, decrement)
    get_response = student_repository.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance - decrement


def test_change_information() -> None:
    student_repository = SqlStudentRepository("")

    first_name = "Peter"
    last_name = "Smith"
    email = "petersmith@gmail.com"
    password = "peter123"
    balance = 50

    new_first_name = "Tim"
    new_last_name = "Murphy"

    student_repository.create_student(first_name, last_name, email, password, balance)
    student_repository.change_first_name(email, new_first_name)
    student_repository.change_last_name(email, new_last_name)

    get_response = student_repository.get_student(email)

    assert isinstance(get_response, Student)
    assert get_response.first_name == new_first_name
    assert get_response.last_name == new_last_name
