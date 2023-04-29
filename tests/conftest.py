import pytest

from app.core.student.interactor import IStudentRepository
from app.infra.inmemory.student import InMemoryStudentRepository


# NOTE: So far, we only use in-memory testing environment.
# TODO: Add tests for SQL implementations.

@pytest.fixture(scope="function")
def student_repository(request: pytest.FixtureRequest) -> IStudentRepository:
    return InMemoryStudentRepository()
