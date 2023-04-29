import pytest
from _pytest.config.argparsing import Parser

from app.core.student.interactor import IStudentRepository
from app.infra.inmemory.student import InMemoryStudentRepository
from app.infra.sqlite.student import SqlStudentRepository


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
