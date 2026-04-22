import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "input_data, state, expected",
    [
        # обычный кейс
        (
            [{"state": "EXECUTED"}, {"state": "PENDING"}],
            "EXECUTED",
            [{"state": "EXECUTED"}],
        ),
        # несколько совпадений
        (
            [{"state": "EXECUTED"}, {"state": "EXECUTED"}],
            "EXECUTED",
            [{"state": "EXECUTED"}, {"state": "EXECUTED"}],
        ),
        # нет совпадений
        (
            [{"state": "PENDING"}],
            "EXECUTED",
            [],
        ),
        # пустой список
        ([], "EXECUTED", []),
        # мусор внутри (dict + не dict)
        (
            [{"state": "EXECUTED"}, "trash", 123, {"state": "EXECUTED"}],
            "EXECUTED",
            [{"state": "EXECUTED"}, {"state": "EXECUTED"}],
        ),
        # нет ключа state
        (
            [{"no_state": "EXECUTED"}, {"state": "EXECUTED"}],
            "EXECUTED",
            [{"state": "EXECUTED"}],
        ),
    ],
)
def test_filter_by_state(input_data, state, expected):
    assert filter_by_state(input_data, state) == expected


@pytest.mark.parametrize(
    "input_data, reverse, expected",
    [
        # по убыванию
        (
            [
                {"date": "2023-01-01"},
                {"date": "2024-01-01"},
            ],
            True,
            [
                {"date": "2024-01-01"},
                {"date": "2023-01-01"},
            ],
        ),
        # по возрастанию
        (
            [
                {"date": "2023-01-01"},
                {"date": "2024-01-01"},
            ],
            False,
            [
                {"date": "2023-01-01"},
                {"date": "2024-01-01"},
            ],
        ),
        # уже отсортировано
        (
            [
                {"date": "2024-01-01"},
                {"date": "2023-01-01"},
            ],
            True,
            [
                {"date": "2024-01-01"},
                {"date": "2023-01-01"},
            ],
        ),
        # пустой список
        ([], True, []),
        # мусор внутри (он должен игнорироваться)
        (
            [
                {"date": "2023-01-01"},
                "trash",
                123,
                {"date": "2024-01-01"},
            ],
            True,
            [
                {"date": "2024-01-01"},
                {"date": "2023-01-01"},
            ],
        ),
        # нет date ключа вообще
        (
            [{"no_date": "2023"}],
            True,
            [],
        ),
    ],
)
def test_sort_by_date(input_data, reverse, expected):
    assert sort_by_date(input_data, reverse) == expected
