import argparse
import csv
import os
from  tabulate import tabulate


DEFAULT_FILENAME = 'products.csv'




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


    # print(table_headers)
    # print(table_data)
    line = []
    for row in table_data:
        line.append(row.values())
    # не хочет список словарей. Только список списков без заголовков
    table = tabulate(tabular_data=line, headers=table_headers, tablefmt='grid')
    print(table)
