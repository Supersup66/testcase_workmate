a = 'apple'
b = 'samsung'
c = '=='

# Создаем выражение для выполнения с использованием eval
expression = f"{a}{c}{b}"

# Выполняем выражение и получаем результат
result = eval(expression)

# Выводим результат сравнения
if result:
    print('da')
else:
    print('net')
