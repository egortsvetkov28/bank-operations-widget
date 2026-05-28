import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.propagate = False


def load_transactions(path: str) -> list:
    """Загрузка транзакций из JSON файла"""

    logger.info(f"Загрузка транзакций из файла: {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

    except FileNotFoundError:
        logger.error("Файл не найден")
        return []

    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON")
        return []

    if not isinstance(data, list):
        logger.warning("JSON не является списком")
        return []

    logger.info("Транзакции успешно загружены")
    return data
