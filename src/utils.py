import json


def load_transactions(path):
    """Загружает список транзакций из JSON-файла. Если ошибка — возвращает []."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if not isinstance(data, list):
        return []

    return data
