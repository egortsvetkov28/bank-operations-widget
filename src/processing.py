def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и возвращает новый список словарей с элементами,
    найденными по ключу "state"
    """
    final_data = []
    for d in data:
        if d["state"] == state:
            final_data.append(d)
    return final_data


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция принимает список словарей и возвращает новый,
    отсортированный список словарей по убыванию список
    """
    final_data = sorted(data, key=lambda x: x["date"], reverse=reverse)
    return final_data
