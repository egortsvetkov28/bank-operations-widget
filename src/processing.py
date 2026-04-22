def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и возвращает новый список словарей с элементами,
    найденными по ключу "state"
    """
    return [d for d in data if isinstance(d, dict) and d.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция принимает список словарей и возвращает новый,
    отсортированный список словарей по убыванию список
    """
    return sorted(
        [d for d in data if isinstance(d, dict) and isinstance(d.get("date"), str)],
        key=lambda x: x["date"],
        reverse=reverse,
    )
