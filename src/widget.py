from .masks import get_mask_account, get_mask_card_number


def mask_account_card(full_info: str) -> str:
    """Принимает строку '{оператор} {номер}' и выводит номера с маской"""

    # сокращенный цикл вывода оператора
    operator_name = "".join(char for char in full_info if not char.isdigit())
    # сокращенный цикл вывода номера карты/счета
    account_number = "".join(char for char in full_info if char.isdigit())

    # определение счет или карта
    if operator_name.startswith("Счет"):
        masked_number = get_mask_account(account_number)
    else:
        masked_number = get_mask_card_number(account_number)

    return f"{operator_name} {masked_number}"


def get_date(date: str) -> str:
    """Принимает полную дату и выводит 'год-месяц-день'"""
    modified_date = "".join(char for char in date if char.isdigit())

    year = modified_date[:4]
    month = modified_date[4:6]
    day = modified_date[6:8]

    return f"{day}.{month}.{year}"
