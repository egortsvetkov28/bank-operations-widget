import pytest
from src.utils import load_transactions


def test_load_transactions_valid_file(tmp_path):
    file = tmp_path / "data.json"
    file.write_text('[{"amount": 100}, {"amount": 200}]', encoding="utf-8")

    result = load_transactions(str(file))

    assert isinstance(result, list)
    assert result == [{"amount": 100}, {"amount": 200}]


def test_load_transactions_file_not_found():
    result = load_transactions("no_such_file.json")

    assert result == []


def test_load_transactions_invalid_json(tmp_path):
    file = tmp_path / "bad.json"
    file.write_text('{"amount": 100', encoding="utf-8")  # битый JSON

    result = load_transactions(str(file))

    assert result == []


def test_load_transactions_not_list(tmp_path):
    file = tmp_path / "not_list.json"
    file.write_text('{"amount": 100}', encoding="utf-8")  # не список

    result = load_transactions(str(file))

    assert result == []
