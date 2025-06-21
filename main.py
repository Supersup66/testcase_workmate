import argparse
import csv
from typing import Any

from tabulate import tabulate

from exceptions import HeaderError, NoOperand

DEFAULT_FILENAME: str = 'products.csv'

AVAILABLE_FILTERS: dict[str, Any] = {
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
    '=': lambda a, b: a == b
}
AVAILABLE_AGGREGATORS: dict[str, Any] = {
    'max': lambda b: max(b),
    'min': lambda b: min(b),
    'avg': lambda b: sum(b) / len(b)
}
AVAILABLE_ORDERING: dict[str, Any] = {
    'asc': lambda table, header: sorted(
        table, key=lambda x: x[header]),
    'desc': lambda table, header: sorted(
        table, key=lambda x: x[header], reverse=True)
}


def read_csv(filename: str) -> list[dict[str, str]]:
    """Считывает файл csv и возвращает список словарей."""
    with open(filename, 'r', encoding='utf-8') as f:
        file_reader = csv.DictReader(f)
        return list(file_reader)


def is_number(s: str) -> bool:
    """Проверяет, возможно ли преобразовать строку в число."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def column_data_to_float(
        table_data: list[dict[str, str]],
        header: str,
        ) -> list[dict[str, str]]:
    """Заменяет значения в столбце на числовые."""

    if is_number(table_data[0][header]):
        for row in table_data:
            row[header] = float(row[header])
    return table_data


def clean_data(raw: str, headers: list[str]) -> tuple[str, str, str]:
    """Разбивает параметр на имя заголовка, операнд, значение.

    Есть проверка на ошибку в операнде и имени заголовка.
    """
    for op in AVAILABLE_FILTERS:
        if op in raw:
            header, value = raw.split(op)
            if header not in headers:
                raise HeaderError(f'Неправильно указано имя столбца: {header}')
            return header, value.lower(), op
    raise NoOperand(
        f'Неправильный операнд: "{op}". '
        f'Операнд должен быть: {", ".join(AVAILABLE_FILTERS.keys())}'
    )


def filter_table(
        table_data: list[dict[str, str]],
        header: str,
        value: str,
        op: str
        ) -> list[dict[str, str]]:
    """Фильтрует данные из таблицы по заданному условию."""

    filtered_data = []
    for row in table_data:
        current_value = row[header]
        if is_number(current_value) and is_number(value):
            current_value = float(current_value)
            value = float(value)
        if AVAILABLE_FILTERS[op](current_value, value):
            filtered_data.append(row)
    return filtered_data


def aggregate_table(
        table_data: list[dict[str, str]],
        header: str,
        value: str
        ) -> list[dict[str, float]]:
    """Агрегирует данные из таблицы по заданному условию."""

    data_for_aggregate = []

    for row in table_data:
        data_for_aggregate.append(float(row[header]))
    result = AVAILABLE_AGGREGATORS[value](data_for_aggregate)
    return [{header: round(result, 2), },]


def order_table(
        table_data: list[dict[str, str]],
        header: str,
        value: str
        ) -> list[dict[str, float]]:
    """Сортирует данные из таблицы по заданному условию."""

    if is_number(table_data[0][header]):
        table_data = column_data_to_float(table_data, header)

    ordered_table = AVAILABLE_ORDERING[value](table_data, header)
    return ordered_table


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='smart .csv parser')

    parser.add_argument(
        '--file',
        type=str,
        help='select .csv file to parse',
        default=DEFAULT_FILENAME
    )
    parser.add_argument(
        '--where',
        type=str,
        help='select filter conditions'
    )
    parser.add_argument(
        '--aggregate',
        type=str,
        help='select aggregate conditions'
    )
    parser.add_argument(
        '--order_by',
        type=str,
        help='select ordering condition'
    )
    args = parser.parse_args()

    working_data: list[dict[str, str]] = read_csv(args.file)
    headers: list[str] = list(working_data[0].keys())

    if args.where:
        header, value, op = clean_data(args.where, headers)
        working_data = filter_table(working_data, header, value, op)

    if args.aggregate:
        header, value, _ = clean_data(args.aggregate, headers)
        working_data = aggregate_table(working_data, header, value)

    if args.order_by:
        header, value, op = clean_data(args.order_by, headers)
        working_data = order_table(working_data, header, value)

    table = tabulate(
        tabular_data=working_data, headers='keys', tablefmt='grid'
    )
    print(table)
