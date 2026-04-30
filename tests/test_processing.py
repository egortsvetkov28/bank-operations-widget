from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


# =========================
# ФИКСТУРА: filter_by_state
# =========================
@pytest.fixture
def state_cases() -> list[tuple[list[Any], str, list[Any]]]:
    return [
        (
            [{"state": "EXECUTED"}, {"state": "PENDING"}],
            "EXECUTED",
            [{"state": "EXECUTED"}],
        ),
        (
            [{"state": "EXECUTED"}, {"state": "EXECUTED"}],
            "EXECUTED",
            [{"state": "EXECUTED"}, {"state": "EXECUTED"}],
        ),
        (
            [{"state": "PENDING"}],
            "EXECUTED",
            [],
        ),
        ([], "EXECUTED", []),
        (
            [{"state": "EXECUTED"}, "trash", 123, {"state": "EXECUTED"}],
            "EXECUTED",
            [{"state": "EXECUTED"}, {"state": "EXECUTED"}],
        ),
        (
            [{"no_state": "EXECUTED"}, {"state": "EXECUTED"}],
            "EXECUTED",
            [{"state": "EXECUTED"}],
        ),
    ]


def test_filter_by_state(state_cases: list[tuple[list[Any], str, list[Any]]]) -> None:
    for input_data, state, expected in state_cases:
        assert filter_by_state(input_data, state) == expected


# =========================
# ФИКСТУРА: sort_by_date
# =========================
@pytest.fixture
def date_cases() -> list[tuple[list[Any], bool, list[Any]]]:
    return [
        (
            [{"date": "2023-01-01"}, {"date": "2024-01-01"}],
            True,
            [{"date": "2024-01-01"}, {"date": "2023-01-01"}],
        ),
        (
            [{"date": "2023-01-01"}, {"date": "2024-01-01"}],
            False,
            [{"date": "2023-01-01"}, {"date": "2024-01-01"}],
        ),
        (
            [{"date": "2024-01-01"}, {"date": "2023-01-01"}],
            True,
            [{"date": "2024-01-01"}, {"date": "2023-01-01"}],
        ),
        ([], True, []),
        (
            [{"date": "2023-01-01"}, "trash", 123, {"date": "2024-01-01"}],
            True,
            [{"date": "2024-01-01"}, {"date": "2023-01-01"}],
        ),
        (
            [{"no_date": "2023"}],
            True,
            [],
        ),
    ]


def test_sort_by_date(date_cases: list[tuple[list[Any], bool, list[Any]]]) -> None:
    for input_data, reverse, expected in date_cases:
        assert sort_by_date(input_data, reverse) == expected
