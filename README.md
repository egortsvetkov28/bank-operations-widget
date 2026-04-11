# Bank Operations Widget

## Цель проекта
Проект предназначен для обработки и анализа банковских операций.  
Модули проекта позволяют фильтровать, сортировать операции, маскировать номера карт и счетов, а также форматировать даты.
---
## Установка
Склонируйте репозиторий и перейдите в директорию проекта:

```bash
git clone https://github.com/egortsvetkov28/bank-operations-widget.git
cd bank-operations-widget
```
Создайте виртуальное окружение и установите зависимости:
```
python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
pip install -r requirements.txt  # если у вас есть зависимости
Использование функций
Маскировка номеров карт и счетов
from src.masks import get_mask_card_number, get_mask_account
from src.processing import mask_account_card
```
---
## Список функций
### Функции масок
```
#маска номера карты
get_mask_card_number("1234567890123456")  # -> '1234 56** **** 3456'
#маска номера счета
get_mask_account("40817810099910004312")  # -> '**4312'

#маска номера счета с оператором
mask_account_card("Счет 40817810099910004312")  # -> 'Счет **4312'
#маска номера карты с оператором
mask_account_card("Visa 1234567890123456")    # -> 'Visa 1234 56** **** 3456'
```
### Фильтрация операций по статусу
```
from src.processing import filter_by_state

operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T10:00:00'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02T11:00:00'}
]

executed_ops = filter_by_state(operations)  # -> оставит только 'EXECUTED'
canceled_ops = filter_by_state(operations, state='CANCELED')  # -> оставит только 'CANCELED'
```
### Сортировка операций по дате
```
from src.processing import sort_by_date

sorted_ops = sort_by_date(operations)  # сортировка по убыванию даты
sorted_ops_asc = sort_by_date(operations, reverse=False)  # сортировка по возрастанию даты
Форматирование даты
from src.processing import get_date

get_date("20230101100000")  # -> '01.01.2023'
```
---
## Структура проекта
```
src/
    __init__.py
    masks.py
    processing.py
    widget.py
tests/
    __init__.py
.gitignore
pyproject.toml
README.md
```
#### Лицензия
*MIT License*