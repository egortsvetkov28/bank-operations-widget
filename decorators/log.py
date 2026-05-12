from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор логирует выполнение функции в консоль или файл."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обёртка функции: логирует результат или ошибку выполнения."""

            def write_log(message: str) -> None:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

            try:
                result = func(*args, **kwargs)
                write_log(f"{func.__name__} ok")
                return result

            except Exception as error:
                write_log(f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator
