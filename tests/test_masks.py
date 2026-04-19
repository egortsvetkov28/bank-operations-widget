import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize(
    "input_data, expected",
    [
        # валидные
        ("1234123412341234", "1234 12** **** 1234"),
        ("123 41234 1234 12 34", "1234 12** **** 1234"),

        # ошибки
        ("", "Введен некорректный номер карты"),
        ("156827", "Введен слишком короткий номер карты"),
        ("reyuegj", "Введен некорректный номер карты"),
        ("%$#*%", "Введен некорректный номер карты"),
        ("1234 12** **** 1234", "Введен некорректный номер карты"),
    ]
)
def test_get_mask_card_number(input_data, expected):
    assert get_mask_card_number(input_data) == expected

@pytest.mark.parametrize(
    "input_data, expected",
    [
        # валидные
        ("1234567890", "**7890"),
        ("9876", "**9876"),

        # ошибки
        ("", "Введен некорректный номер счета"),
        ("123", "Введен некорректный номер счета"),
        (None, "Введен некорректный номер счета"),
    ]
)
def test_get_mask_account(input_data, expected):
    assert get_mask_account(input_data) == expected