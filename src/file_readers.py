from typing import Any, cast

import pandas as pd


def read_csv_transactions(path: str) -> list[dict[str, Any]]:
    """Читает транзакции из CSV-файла."""
    df = pd.read_csv(path)
    return cast(list[dict[str, Any]], df.to_dict(orient="records"))


def read_excel_transactions(path: str) -> list[dict[str, Any]]:
    """Читает транзакции из Excel-файла."""
    df = pd.read_excel(path)
    return cast(list[dict[str, Any]], df.to_dict(orient="records"))
