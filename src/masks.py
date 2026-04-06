def get_mask_card_number(card_number: str) -> str:
    """Функция приема номера карты пользователя"""
    edit_card_number = ""
    for i in range(len(card_number)):
        if 6 <= i < len(card_number) - 4:
            edit_card_number += "*"
        else:
            edit_card_number += card_number[i]

        if (i + 1) % 4 == 0 and i != len(card_number) - 1:
            edit_card_number += " "

    return edit_card_number


def get_mask_account(account_number: str) -> str:
    """Функция приема номера счета пользователя"""
    return f"**{account_number[-4:]}"
