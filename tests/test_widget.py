from typing import Any

import pytest

from src.widget import get_date, mask_account_card


# =========================
# ФИКСТУРА: карты / счета
# =========================
@pytest.fixture
def card_cases() -> list[tuple[str, str]]:
    return [
        ("Visa Classic 1234123412341234", "Visa Classic 1234 12** **** 1234"),
        ("MasterCard 5555555555554444", "MasterCard 5555 55** **** 4444"),
        ("Счет 1234567890", "Счет **7890"),
        ("Visa!!! 1234 1234 1234 1234", "Visa!!! 1234 12** **** 1234"),
        ("  Visa Classic   1234123412341234  ", "Visa Classic 1234 12** **** 1234"),
        ("Visa ABCD", "Visa ABCD"),
        ("Visa 1234", "Visa 1234"),
    ]


# =========================
# TEST mask_account_card
# =========================
def test_mask_account_card(card_cases: list[tuple[str, str]]) -> None:
    for input_data, expected in card_cases:
        assert mask_account_card(input_data) == expected


# edge-case защита
@pytest.mark.parametrize(
    "bad_input: Any",
    [
        None,
        "",
        "   ",
    ],
)
def test_mask_account_card_bad_input(bad_input: Any) -> None:
    assert mask_account_card(bad_input) == ""


# =========================
# ФИКСТУРА: даты
# =========================
@pytest.fixture
def date_cases() -> list[tuple[Any, str]]:
    return [
        ("2024-01-01T12:30:00", "01.01.2024"),
        ("2023-12-31T00:00:00", "31.12.2023"),
        ("20240101", "01.01.2024"),
        ("2024-07-15", "15.07.2024"),
        ("Дата: 2024-01-01 время 12:00", "01.01.2024"),
        ("2024", ""),
        ("", ""),
        (None, ""),
    ]


# =========================
# TEST get_date
# =========================
def test_get_date(date_cases: list[tuple[Any, str]]) -> None:
    for input_data, expected in date_cases:
        assert get_date(input_data) == expected
