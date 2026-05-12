from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """
    Генератор, который фильтрует транзакции по заданной валюте.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который возвращает описания транзакций.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_number: int, end_number: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в заданном диапазоне.
    """
    for number in range(start_number, end_number + 1):
        card = f"{number:016d}"
        yield f"{card[0:4]} {card[4:8]} {card[8:12]} {card[12:16]}"