import random
import csv

# Расширенный набор продуктов и производителей
products = [
    "Хлеб белый",
    "Хлеб черный",
    "Молоко пастеризованное",
    "Кефир жирный",
    "Творог зерненый",
    "Масло сливочное",
    "Сметана домашняя",
    "Майонез натуральный",
    "Сыр российский",
    "Сыр голландский",
    "Колбаса вареная",
    "Колбаса сырокопченая",
    "Шоколад молочный",
    "Конфеты карамельные",
    "Печенье овсяное",
    "Мед натуральный",
    "Свинина охлажденная",
    "Курица фермерская",
    "Рыба мороженная",
    "Морковь свежая",
    "Капуста белокочанная",
    "Огурцы свежие",
    "Томаты грунтовые",
    "Лук репчатый",
    "Яблоки зеленые",
    "Бананы спелые",
    "Клубника садовая",
    "Арбузы сладкие",
]

manufacturers = [
    "ООО 'Простор'",
    "ЗАО 'Сибирские продукты'",
    "Фермерское хозяйство 'Удача'",
    "ПКФ 'Натуральный продукт'",
    "Компания 'Экоферма'",
    "Агрофирма 'Дар земли'",
    "Производственная компания 'Родник'",
    "Завод 'Живая еда'",
    "СПК 'Русские деликатесы'",
    "ИП Петров",
    "Индивидуальное предприятие Иванов",
    "Семейная ферма 'Цветочная долина'"
]

# Функция для генерации одной случайной строки
def generate_random_row():
    product_name = random.choice(products)
    manufacturer = random.choice(manufacturers)
    weight = round(random.uniform(0.1, 5), 2)
    price = round(random.uniform(10, 100), 2)
    article_number = f"{random.randint(1, 1000)}-{product_name[:3].upper()}"
    return {
        'name': product_name,
        'manufacturer': manufacturer,
        'weight': weight,
        'price': price,
        'article': article_number
    }

# Открываем файл для записи и создаем объект writer
with open('random.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['name', 'manufacturer', 'weight', 'price', 'article']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Записываем заголовки
    writer.writeheader()
    
    # Заполняем 1000 строк случайными данными
    for _ in range(1000):
        row = generate_random_row()
        writer.writerow(row)
