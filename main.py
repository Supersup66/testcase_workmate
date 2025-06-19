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
        

def clean_data(raw, table_headers):
    """Разбивает параметр на имя заголовка, операнд, значение.
    
    Есть проверка на отсутствие операнда.
    Нужно дописать проверку на несколько операндов чтобы не выдавал 
    ('Brand<', '6', '>')
    """
    for op in AVAILABLE_FILTERS:
        if op in raw:
            # try:
            header, value = raw.split(op)
            #     # value = float(value) if '.' in value else int(value)
            # except ValueError as e:
            #     print(f'В заданном условии {raw} содержится ошибка: {e}')
            #     # return
            # if header not in table_headers:
            #     print(f'Неверно указано имя столбца: {header}')
            #     return
            return header, value, op
    print(f'Не указан, либо неверно указан операнд. '
          f'Операнд должен быть {AVAILABLE_FILTERS.keys()}')
    return


def filter_table(table_data, header, value, op):
    filtered_data = []

    for row in table_data:
        current_value = row[header]
        if AVAILABLE_FILTERS[op](current_value, value):
            filtered_data.append(row)
    return filtered_data


def aggregate_table(working_data, header, value):
    data_for_aggregate = []

    for row in working_data:
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


    with open(args.file, 'r', encoding='utf-8') as f:
        file_reader = csv.DictReader(f)
        # print(list(file_reader))
        # for row in file_reader:
        #     print('Строка: \n')
        #     print(row)
        # формируем таблицу как список словарей
        table_data = list(file_reader)
        table_headers = table_data[0].keys()
    
    # потом убрать
    working_data = table_data
    table = tabulate(tabular_data=working_data, headers='keys', tablefmt='grid')
    print(table)    
    if args.where:
        print('есть фильтр')
        #print(clean_data(args.where, table_headers))
        if clean_data(args.where, table_headers):
            header, value, op = clean_data(args.where, table_headers)
            working_data = filter_table(working_data, header, value, op)
    table = tabulate(tabular_data=working_data, headers='keys', tablefmt='grid')
    print('после фильтрации')
    print(table)
    if args.aggregate:
        print('есть агрегатор')
        if clean_data(args.aggregate, table_headers):
            header, value, op = clean_data(args.aggregate, table_headers)
            working_data = aggregate_table(working_data, header, value)

    print('результат')

    # print(table_headers)
    # print(table_data)
    # line = []
    # for row in working_data:
    #     # print(row)
    #     line.append(row.values())
    # не хочет список словарей. Только список списков без заголовков
    table = tabulate(tabular_data=working_data, headers='keys', tablefmt='grid')
    print(table)
