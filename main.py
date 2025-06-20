import argparse
import csv
from tabulate import tabulate


DEFAULT_FILENAME = 'products.csv'

AVAILABLE_FILTERS = {
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
    '=': lambda a, b: a == b
}
AVAILABLE_AGGREGATORS = {
    'max': lambda b: max(b),
    'min': lambda b: min(b),
    'avg': lambda b: sum(b) / len(b)
}


def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        file_reader = csv.DictReader(f)
        return list(file_reader)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def clean_data(raw, headers):
    """Разбивает параметр на имя заголовка, операнд, значение.
    
    Есть проверка на отсутствие операнда.
    Нужно дописать проверку на несколько операндов чтобы не выдавал 
    ('Brand<', '6', '>')
    """
    for op in AVAILABLE_FILTERS:
        if op in raw:
            header, value = raw.split(op)
            if header not in headers:
                print(f'Неверно указано имя столбца: {header}')
                return
            return header, value, op
    print(f'Не указан, либо неверно указан операнд. '
          f'Операнд должен быть {AVAILABLE_FILTERS.keys()}')
    return


def filter_table(table_data, header, value, op):
    filtered_data = []

    for row in table_data:
        current_value = row[header]
        if is_number(current_value) and is_number(value):
            current_value = float(current_value)
            value = float(value)
        if AVAILABLE_FILTERS[op](current_value, value):
            filtered_data.append(row)
    return filtered_data


def aggregate_table(table_data, header, value):
    data_for_aggregate = []

    for row in table_data:
        data_for_aggregate.append(float(row[header]))
    result = AVAILABLE_AGGREGATORS[value](data_for_aggregate)
    return [{header: round(result, 2), },]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='smart .csv parser')

    parser.add_argument('--file', type=str, help='select .csv file to parse', default=DEFAULT_FILENAME)
    parser.add_argument('--where', type=str, help='select filter conditions')
    parser.add_argument('--aggregate', type=str, help='select aggregate conditions')

    # Передаем в переменную полученные аргументы
    # Переменная имеет вид 
    # Namespace(file='products.csv', where=None, aggregate=None)
    args = parser.parse_args()

    working_data = read_csv(args.file)
    headers = working_data[0].keys()

    if args.where and clean_data(args.where, headers):
        header, value, op = clean_data(args.where)
        working_data = filter_table(working_data, header, value, op)
    else:
        working_data = []

    if args.aggregate and clean_data(args.aggregate, headers):
        header, value, _ = clean_data(args.aggregate)
        working_data = aggregate_table(working_data, header, value)
    else:
        working_data = []

    # не хочет список словарей. Только список списков без заголовков
    table = tabulate(tabular_data=working_data, headers='keys', tablefmt='grid')
    print(table)
