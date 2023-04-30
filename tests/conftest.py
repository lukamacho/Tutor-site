import pytest
from _pytest.config.argparsing import Parser

from app.core.course.interactor import ICourseRepository
from app.core.student.interactor import IStudentRepository
from app.core.tutor.interactor import ITutorRepository
from app.infra.inmemory.course import InMemoryCourseRepository
from app.infra.inmemory.student import InMemoryStudentRepository
from app.infra.inmemory.tutor import InMemoryTutorRepository
from app.infra.sqlite.course import SqlCourseRepository
from app.infra.sqlite.student import SqlStudentRepository
from app.infra.sqlite.tutors import SqlTutorRepository


def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        "--sql",
        action="store_true",
        default=False,
        help="",
    )


def use_sql(request: pytest.FixtureRequest) -> bool:
    return request.config.getoption("--sql")


@pytest.fixture(scope="function")
def student_repository(request: pytest.FixtureRequest) -> IStudentRepository:
    if use_sql(request):
        return SqlStudentRepository("")
    return InMemoryStudentRepository()


@pytest.fixture(scope="function")
def tutor_repository(request: pytest.FixtureRequest) -> ITutorRepository:
    if use_sql(request):
        return SqlTutorRepository("")
    return InMemoryTutorRepository()


@pytest.fixture(scope="function")
def course_repository(request: pytest.FixtureRequest) -> ICourseRepository:
    if use_sql(request):
        return SqlCourseRepository("")
    return InMemoryCourseRepository()
