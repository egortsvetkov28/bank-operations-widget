import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("API_KEY is not set in environment variables")

# 🔥 ВАЖНО: сужаем тип для mypy
assert API_KEY is not None


def get_exchange_rate(currency: str) -> float:
    """Возвращает курс валюты к RUB через внешний API."""

    if currency == "RUB":
        return 1.0

    url = "https://api.apilayer.com/exchangerates_data/latest"

    headers: dict[str, str] = {"apikey": API_KEY}

    params: dict[str, str] = {"base": currency, "symbols": "RUB"}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    return float(data["rates"]["RUB"])


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли."""

    amount = transaction["amount"]
    currency = transaction["currency"]

    rate = get_exchange_rate(currency)

    return float(amount) * rate
