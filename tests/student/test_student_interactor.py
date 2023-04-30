from app.core.student.interactor import StudentInteractor, IStudentRepository
from app.core.student.entity import Student


def test_create_student(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    response = interactor.create_student("John", "Doe", "johndoe@gmail.com", "johndoe", 50)

    assert isinstance(response, Student)
    assert student_repository.get_student("johndoe@gmail.com") is not None
    assert student_repository.get_student("") is None


def test_create_students(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    for i in range(10000):
        mail = "johndoe{i}@gmail.com".format(i=i)
        response = interactor.create_student("John", "Doe", mail, "johndoe", 0)
        assert isinstance(response, Student)
        assert student_repository.get_student(mail) is not None


def test_get_student(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    first_name = "Mia"
    last_name = "Seaworth"
    email = "miaseaworth@gmail.com"
    password = "mia123"
    balance = 100

    interactor.create_student(first_name, last_name, email, password, balance)
    get_response = interactor.get_student(email)

    assert isinstance(get_response, Student)
    assert get_response.first_name == first_name
    assert get_response.last_name == last_name
    assert get_response.email == email
    assert get_response.password == password
    assert get_response.balance == balance

    new_email = "idontexist@gmail.com"

    get_response = interactor.get_student(new_email)

    assert get_response is None


def test_set_balance(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    first_name = "Nina"
    last_name = "Fanning"
    email = "ninafanning@gmail.com"
    password = "nina123"
    balance = 50

    new_balance = 100

    interactor.create_student(first_name, last_name, email, password, balance)
    interactor.set_balance(email, new_balance)
    get_response = interactor.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance

    new_balance = 150

    interactor.set_balance(email, new_balance)
    get_response = interactor.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance


def test_change_balance(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    first_name = "Emma"
    last_name = "Murdoch"
    email = "emmamurdoch@gmail.com"
    password = "emma123"
    balance = 0

    increment = 60

    interactor.create_student(first_name, last_name, email, password, balance)
    interactor.increase_balance(email, increment)
    get_response = interactor.get_balance(email)

    new_balance = balance + increment

    assert isinstance(get_response, int)
    assert get_response == new_balance

    decrement = 50

    interactor.decrease_balance(email, decrement)
    get_response = interactor.get_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance - decrement


def test_change_information(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    first_name = "Peter"
    last_name = "Smith"
    email = "petersmith@gmail.com"
    password = "peter123"
    balance = 50

    new_first_name = "Tim"
    new_last_name = "Murphy"

    interactor.create_student(first_name, last_name, email, password, balance)
    interactor.change_first_name(email, new_first_name)
    interactor.change_last_name(email, new_last_name)

    get_response = interactor.get_student(email)

    assert isinstance(get_response, Student)
    assert get_response.first_name == new_first_name
    assert get_response.last_name == new_last_name
