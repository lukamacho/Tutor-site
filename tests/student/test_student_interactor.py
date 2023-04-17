from app.core.student.interactor import StudentInteractor

def test_create_student() -> None:
    interactor = StudentInteractor()
    email = "daenerys@gmail.com"
    password = "dragons"

    response = interactor.create_student(email, password)

    assert response is None
