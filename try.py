def is_number(s: str) -> bool:
    """Проверяет, явлчется ли переменная десятичным числом."""
    try:
        float(s)
        return True
    except ValueError:
        return False

def sort_table(table, key):
    """
    Сортирует список словарей по указанному ключу.

    :param table: Список словарей, представляющих таблицу.
    :param key: Ключ (поле), по которому осуществляется сортировка.
    :return: Отсортированный список словарей.
    """
    return sorted(table, key=lambda x: x[key])

def column_data_to_float(table_data, header):
    if is_number(table_data[0][header]):
        for row in table_data:
            row[header] = float(row[header])
    return print(table_data)


sorters = {
    'asc': lambda table, header: sorted(table, key=lambda x: x[header]),
    'desc': lambda table, header: sorted(table, key=lambda x: x[header], reverse=True) 
}
table = [
    {'name': 'Иван', 'age': '25'},
    {'name': 'Анна', 'age': '30'},
    {'name': 'Михаил', 'age': '20'}
]
header = 'name'
value = 'asc'

result = sorters[value](table, header)
print(result)
