import pytest


@pytest.fixture(scope="class")
def log_file(request):
    log_file = request.config.getoption("--log-file")
    yield log_file
