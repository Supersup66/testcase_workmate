a = 'apple'
b = [i for i in range(11)]
c = 'avg'

# Создаем выражение для выполнения с использованием eval
expression = {'max': lambda b: max(b),
              'min': lambda b: min(b),
              'avg': lambda b: sum(b) / len(b)}

# Выполняем выражение и получаем результат


print(expression[c](b))
