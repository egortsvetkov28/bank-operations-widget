import pytest

from decorators.log import log


def test_log_success_console(capsys):
    """Проверяет успешный лог в консоль."""

    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)

    captured = capsys.readouterr()

    assert result == 3
    assert "add ok" in captured.out


def test_log_error_console(capsys):
    """Проверяет лог ошибки в консоль."""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "divide error" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_success_file(tmp_path):
    """Проверяет успешный лог в файл."""

    file = tmp_path / "log.txt"

    @log(filename=str(file))
    def add(a, b):
        return a + b

    result = add(2, 3)

    content = file.read_text(encoding="utf-8")

    assert result == 5
    assert "add ok" in content


def test_log_error_file(tmp_path):
    """Проверяет лог ошибки в файл."""

    file = tmp_path / "log.txt"

    @log(filename=str(file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    content = file.read_text(encoding="utf-8")

    assert "divide error" in content
    assert "Inputs: (1, 0), {}" in content
