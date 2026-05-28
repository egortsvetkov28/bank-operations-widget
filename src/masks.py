import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.propagate = False


def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера карты"""

    logger.info("Начало обработки номера карты")

    if not card_number:
        logger.error("Пустой номер карты")
        return "Введен некорректный номер карты"

    if not all(char.isdigit() or char.isspace() for char in card_number):
        logger.error("Некорректные символы в номере карты")
        return "Введен некорректный номер карты"

    card_number = card_number.replace(" ", "")

    if len(card_number) < 10:
        logger.error("Слишком короткий номер карты")
        return "Введен слишком короткий номер карты"

    result = ""

    for i in range(len(card_number)):
        if 6 <= i < len(card_number) - 4:
            result += "*"
        else:
            result += card_number[i]

        if (i + 1) % 4 == 0 and i != len(card_number) - 1:
            result += " "

    logger.info("Успешная маскировка карты")
    return result


def get_mask_account(account_number: str) -> str:
    """Маскировка номера счета"""

    logger.info("Начало обработки счета")

    if not account_number or len(account_number) < 4:
        logger.error("Некорректный номер счета")
        return "Введен некорректный номер счета"

    result = f"**{account_number[-4:]}"

    logger.info("Успешная маскировка счета")
    return result
