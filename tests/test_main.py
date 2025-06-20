import pytest

import main


def test_read_csv(csv_filename, table_data):
    """Тест наличия csv файла."""
    assert main.read_csv(csv_filename) == table_data


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
            ('rating', 'avg', [{'rating': 4.49}]),
            ('price', 'min', [{'price': 149.0}]),
        ]
)
def test_aggregate_table(table_data, header, value, result):
    """Тест аггрегации данных таблицы."""
    assert main.aggregate_table(table_data, header, value) == result
