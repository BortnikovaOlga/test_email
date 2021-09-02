import traceback

import pytest


def is_valid_email(email: str) -> bool:
    """Проверяет корректность строки email."""
    import re

    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def log(file_name: str, text: str) -> None:
    """Добовляет text в файл file_name."""
    with open(file_name, "a") as f:
        f.write(text)


def get_function_name() -> str:
    """Возвращает имя выполняемой функции."""
    return traceback.extract_stack(None, 2)[0][2]


class TestEmail:
    """
    Тест для списка email.
    """

    @pytest.mark.parametrize(
        ("email", "result"),
        [
            ("test@test.ru", True),
            ("w@w.com", True),
            ("123QWE@mmm.mmm", True),
            ("test@test.", False),
            ("w@", True),
            ("@tt", False),
        ],
    )
    def test_valid_email(self, log_file, email, result):
        """Параметризируется парами (проверяемый email, ожидаемый результат проверки).
        Результат тестов записывается в log_file - задано опцией --log-file в pytest.ini."""
        try:
            result_test = __name__ + "::" + get_function_name() + "[" + email
            assert is_valid_email(email) == result
            result_test += "] PASSED\n"
        except Exception as ex:
            result_test += "] FAILED\n"
            raise ex
        finally:
            log(log_file, result_test)
