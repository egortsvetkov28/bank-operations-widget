from .masks import get_mask_account, get_mask_card_number


def mask_account_card(full_info: str) -> str:
    """Принимает строку 'Оператор Номер' и возвращает замаскированный результат"""

    if not isinstance(full_info, str) or not full_info.strip():
        return ""

    parts = full_info.split()

    operator_name = " ".join([p for p in parts if not any(c.isdigit() for c in p)])

    number = "".join(char for char in full_info if char.isdigit())

    # если цифр нет → вернуть как есть
    if not number:
        return full_info

    # короткий номер НЕ обрабатываем вообще
    if len(number) < 6:
        return full_info

    # счёт
    if "Счет" in operator_name:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{operator_name} {masked_number}"


def get_date(date: str) -> str:
    """Преобразует дату в формат DD.MM.YYYY"""

    if not isinstance(date, str):
        return ""

    digits = "".join(char for char in date if char.isdigit())

    if len(digits) < 8:
        return ""

    return f"{digits[6:8]}.{digits[4:6]}.{digits[:4]}"
