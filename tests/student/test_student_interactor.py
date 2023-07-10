from app.core.student.entity import Student
from app.core.student.interactor import IStudentRepository, StudentInteractor


def test_create_student(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    mail = "johndoe@gmail.com"

    response = interactor.create_student("John", "Doe", mail, "johndoe", 50)

    assert isinstance(response, Student)
    assert student_repository.get_student(mail) is not None
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
    interactor.set_student_balance(email, new_balance)
    get_response = interactor.get_student_balance(email)

    assert isinstance(get_response, int)
    assert get_response == new_balance

    new_balance = 150

    interactor.set_student_balance(email, new_balance)
    get_response = interactor.get_student_balance(email)

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
    interactor.increase_student_balance(email, increment)
    get_response = interactor.get_student_balance(email)

    new_balance = balance + increment

    assert isinstance(get_response, int)
    assert get_response == new_balance

    decrement = 50

    interactor.decrease_student_balance(email, decrement)
    get_response = interactor.get_student_balance(email)

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
    interactor.change_student_first_name(email, new_first_name)
    interactor.change_student_last_name(email, new_last_name)

    get_response = interactor.get_student(email)

    assert isinstance(get_response, Student)
    assert get_response.first_name == new_first_name
    assert get_response.last_name == new_last_name


def test_change_password(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    first_name = "Anne"
    last_name = "Warwick"
    email = "annewarwick@gmail.com"
    password = "anne123"
    new_password = "anne1234"
    balance = 0

    response = interactor.create_student(
        first_name, last_name, email, password, balance
    )

    assert isinstance(response, Student)
    assert response.first_name == first_name
    assert response.last_name == last_name
    assert response.email == email
    assert response.password == password
    assert response.balance == balance

    interactor.change_student_password(email, new_password)
    response = interactor.get_student(email)
    assert response.email == email
    assert response.password == new_password


def test_change_profile_address(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    first_name = "Anne"
    last_name = "Warwick"
    email = "annewarwick@gmail.com"
    password = "anne123"
    balance = 0
    profile_address = "/annewarwick"
    response = interactor.create_student(
        first_name, last_name, email, password, balance
    )

    assert isinstance(response, Student)
    assert response.first_name == first_name
    assert response.last_name == last_name
    assert response.email == email
    assert response.password == password
    assert response.balance == balance
    assert response.profile_address == ""

    interactor.change_student_profile_address(email, profile_address)
    response = interactor.get_student(email)
    assert response.profile_address == profile_address


def test_delete_student(student_repository: IStudentRepository) -> None:
    interactor = StudentInteractor(student_repository)

    first_name = "Anne"
    last_name = "Warwick"
    email = "annewarwick@gmail.com"
    password = "anne123"
    balance = 0

    response = interactor.create_student(
        first_name, last_name, email, password, balance
    )

    assert isinstance(response, Student)
    assert response.first_name == first_name
    assert response.last_name == last_name
    assert response.email == email
    assert response.password == password
    assert response.balance == balance

    interactor.delete_student(email)
    response = interactor.get_student(email)
    assert response.first_name == ""
    assert response.last_name == ""
    assert response.email == ""
    assert response.password == ""
    assert response.balance == 0
