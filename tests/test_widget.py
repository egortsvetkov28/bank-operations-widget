import pytest
from src.widget import mask_account_card, get_date

# =========================
# mask_account_card
# =========================


@pytest.mark.parametrize(
    "input_data, expected",
    [
        # нормальная карта
        (
            "Visa Classic 1234123412341234",
            "Visa Classic 1234 12** **** 1234",
        ),
        (
            "MasterCard 5555555555554444",
            "MasterCard 5555 55** **** 4444",
        ),
        # счёт
        (
            "Счет 1234567890",
            "Счет **7890",
        ),
        # мусор в названии (цифры есть → маска работает)
        (
            "Visa!!! 1234 1234 1234 1234",
            "Visa!!! 1234 12** **** 1234",
        ),
        # пробелы
        (
            "  Visa Classic   1234123412341234  ",
            "Visa Classic 1234 12** **** 1234",
        ),
        # нет цифр → возвращается как есть
        (
            "Visa ABCD",
            "Visa ABCD",
        ),
        # слишком короткий номер → тоже как есть (ВАЖНО ДЛЯ COVERAGE)
        (
            "Visa 1234",
            "Visa 1234",
        ),
        # пустая строка
        (
            "",
            "",
        ),
        # только пробелы
        (
            "   ",
            "",
        ),
        # не строка
        (
            None,
            "",
        ),
    ],
)
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


# =========================
# get_date
# =========================


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("2024-01-01T12:30:00", "01.01.2024"),
        ("2023-12-31T00:00:00", "31.12.2023"),
        ("20240101", "01.01.2024"),
        ("2024-07-15", "15.07.2024"),
        ("Дата: 2024-01-01 время 12:00", "01.01.2024"),
        # мусор → пусто
        ("2024", ""),
        ("", ""),
        (None, ""),
    ],
)
def test_get_date(input_data, expected):
    assert get_date(input_data) == expected
