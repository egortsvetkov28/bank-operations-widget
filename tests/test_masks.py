from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


# =========================
# ФИКСТУРА: карты
# =========================
@pytest.fixture
def card_cases() -> list[tuple[str, str]]:
    return [
        ("1234123412341234", "1234 12** **** 1234"),
        ("123 41234 1234 12 34", "1234 12** **** 1234"),
        ("", "Введен некорректный номер карты"),
        ("156827", "Введен слишком короткий номер карты"),
        ("reyuegj", "Введен некорректный номер карты"),
        ("%$#*%", "Введен некорректный номер карты"),
        ("1234 12** **** 1234", "Введен некорректный номер карты"),
    ]


# =========================
# TEST card
# =========================
def test_get_mask_card_number(card_cases: list[tuple[str, str]]) -> None:
    for input_data, expected in card_cases:
        assert get_mask_card_number(input_data) == expected


# =========================
# ФИКСТУРА: счета
# =========================
@pytest.fixture
def account_cases() -> list[tuple[Any, str]]:
    return [
        ("1234567890", "**7890"),
        ("9876", "**9876"),
        ("", "Введен некорректный номер счета"),
        ("123", "Введен некорректный номер счета"),
        (None, "Введен некорректный номер счета"),
    ]


# =========================
# TEST account
# =========================
def test_get_mask_account(account_cases: list[tuple[Any, str]]) -> None:
    for input_data, expected in account_cases:
        assert get_mask_account(input_data) == expected
