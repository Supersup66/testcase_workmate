DEFAULT_FILENAME = 'products.csv'
FILTER_OPERAND = ['>', '<', '=']
raw = 'brand=>0'
header_list = ['brand', 'name', 'price']

def clean_data(raw):
    """Разбивает параметр --where на имя заголовка, операнд, значение.
    
    Есть проверка на отсутствие операнда.
    Нужно дописать проверку на несколько операндов чтобы не выдавал 
    ('Brand<', '6', '>')
    """
    for op in FILTER_OPERAND:
        if op in raw:
            try:
                header, value = raw.split(op)
                value = float(value) if '.' in value else int(value)
            except ValueError as e:
                print(f'В заданном условии {raw} содержится ошибка: {e}')
                return
            if header not in header_list:
                print(f'Неверно указано имя столбца: {header}')
                return
            return header, value, op
    print(f'Не указан, либо неверно указан операнд. '
          f'Операнд должен быть {FILTER_OPERAND}')
    return


if clean_data(raw):
    header, value, op = clean_data(raw)
    print(header, value, op)
else:
    print('Что-то пошло не так')