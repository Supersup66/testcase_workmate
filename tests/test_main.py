import pytest

import main


def test_read_csv(csv_filename, table_data):
    """Тест наличия csv файла."""
    assert main.read_csv(csv_filename) == table_data


@pytest.mark.parametrize(
        'value, result', [
            ('134', True),
            ('6.23', True),
            ('some', False),
            ('13C', False)
        ]
)
def test_in_number(value, result):
    """Тест определения числовых значений."""
    assert main.is_number(value) == result


@pytest.mark.parametrize(
        'raw, header, value, op', [
            ('brand=apple', 'brand', 'apple', '='),
            ('price>149', 'price', '149', '>'),
            ('rating=avg', 'rating', 'avg', '='),
            ('price=149', 'price', '149', '=')
        ]
)
def test_clean_data(table_data, raw, header, value, op):
    """Тест преобразования запроса."""
    headers = table_data[0].keys()
    assert main.clean_data(raw, headers) == (header, value, op)


@pytest.mark.parametrize(
        'header, value, op, result', [
            ('name', 'redmi note 12', '=',
             [{'brand': 'xiaomi',
               'name': 'redmi note 12',
               'price': '199',
               'rating': '4.6'}]),

            ('price', '1000', '>',
             [{'brand': 'samsung',
               'name': 'galaxy s23 ultra',
               'price': '1199',
               'rating': '4.8'}]),

            ('price', '149', '=',
             [{'brand': 'xiaomi',
               'name': 'redmi 10c',
               'price': '149',
               'rating': '4.1'}]),
        ]
)
def test_filter_table(table_data, header, value, op, result):
    """Тест фильтрации данных таблицы."""
    assert main.filter_table(table_data, header, value, op) == result


@pytest.mark.parametrize(
        'header, value, result', [
            ('price', 'max', [{'price': 1199.0}]),
            ('rating', 'min', [{'rating': 4.1}]),
            ('rating', 'avg', [{'rating': 4.62}]),
            ('price', 'min', [{'price': 149.0}]),
        ]
)
def test_aggregate_table(table_data, header, value, result):
    """Тест аггрегации данных таблицы."""
    assert main.aggregate_table(table_data, header, value) == result


@pytest.mark.parametrize(
        'header, type', [
            ('price', float),
            ('name', str)
        ]
)
def test_column_data_to_float(table_data, header, type):
    """Тест конвертации значиний столбца в число."""
    assert isinstance(table_data[0][header], str) is True
    converted_table = main.column_data_to_float(table_data, header)
    assert isinstance(converted_table[0][header], type) is True


@pytest.mark.parametrize(
        'header, value, result', [
            ('name', 'desc', [
                {'name': 'redmi note 12', 'brand': 'xiaomi',
                 'price': '199', 'rating': '4.6'},
                {'name': 'redmi 10c', 'brand': 'xiaomi',
                 'price': '149', 'rating': '4.1'},
                {'name': 'iphone 15 pro', 'brand': 'apple',
                 'price': '999', 'rating': '4.9'},
                {'name': 'iphone 14', 'brand': 'apple',
                 'price': '799', 'rating': '4.7'},
                {'name': 'galaxy s23 ultra', 'brand': 'samsung',
                 'price': '1199', 'rating': '4.8'}]),
            ('rating', 'asc', [
                {'name': 'redmi 10c', 'brand': 'xiaomi',
                 'price': '149', 'rating': 4.1},
                {'name': 'redmi note 12', 'brand': 'xiaomi',
                 'price': '199', 'rating': 4.6},
                {'name': 'iphone 14', 'brand': 'apple',
                 'price': '799', 'rating': 4.7},
                {'name': 'galaxy s23 ultra', 'brand': 'samsung',
                 'price': '1199', 'rating': 4.8},
                {'name': 'iphone 15 pro', 'brand': 'apple',
                 'price': '999', 'rating': 4.9}])
        ]
)
def test_ordering_table(table_data, header, value, result):

    if main.is_number(table_data[0][header]):
        table_data = main.column_data_to_float(table_data, header)

    ordered_table = main.AVAILABLE_ORDERING[value](table_data, header)
    assert ordered_table == result
