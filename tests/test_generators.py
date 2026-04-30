import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)

# ---------------- FIXTURES ----------------


@pytest.fixture
def transactions():
    return [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "A"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "B"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "C"},
    ]


# ---------------- PARAMETRIZED TESTS ----------------


@pytest.mark.parametrize(
    "currency, expected_len",
    [
        ("USD", 2),
        ("EUR", 1),
        ("GBP", 0),
    ],
)
def test_filter_by_currency(transactions, currency, expected_len):
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_len


# ---------------- GENERATOR TEST ----------------


def test_transaction_descriptions(transactions):
    gen = transaction_descriptions(transactions)
    result = list(gen)

    assert result == ["A", "B", "C"]


# ---------------- CARD GENERATOR ----------------


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        )
    ],
)
def test_card_number_generator(start, end, expected):
    gen = card_number_generator(start, end)
    result = list(gen)

    assert result == expected
