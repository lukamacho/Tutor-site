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

