import pytest
from unittest.mock import patch

from src.external_api import get_exchange_rate, convert_to_rub


# RUB без обращения к API
def test_get_exchange_rate_rub():
    assert get_exchange_rate("RUB") == 1.0


# USD через mock внешнего API
@patch("src.external_api.requests.get")
def test_get_exchange_rate_usd(mock_get):
    mock_get.return_value.json.return_value = {
        "rates": {"RUB": 90}
    }

    result = get_exchange_rate("USD")

    assert result == 90.0


# конвертация USD в рубли
@patch("src.external_api.get_exchange_rate")
def test_convert_to_rub_usd(mock_rate):
    mock_rate.return_value = 90

    transaction = {
        "amount": 10,
        "currency": "USD"
    }

    result = convert_to_rub(transaction)

    assert result == 900.0


# конвертация RUB (без конвертации)
@patch("src.external_api.get_exchange_rate")
def test_convert_to_rub_rub(mock_rate):
    mock_rate.return_value = 1

    transaction = {
        "amount": 100,
        "currency": "RUB"
    }

    result = convert_to_rub(transaction)

    assert result == 100.0