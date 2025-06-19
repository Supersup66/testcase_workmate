import csv
from tabulate import tabulate

with open('products.csv', 'r', encoding='utf-8') as f:
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

def filter_table(table_data, header, value, op):
    filtered_data = []

    for row in table_data:
        current_value = row[header]
        if eval(f'{current_value}{op}{value}'):
            filtered_data.append(row)
    return filtered_data


working_data = filter_table(working_data, 'brand', 'samsung', '==')

table = tabulate(tabular_data=working_data, headers='keys', tablefmt='grid')
print(table)
