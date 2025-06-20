import pytest

from .. import main  # read_csv, clean_data, filter_table, aggregate_table


def test_read_csv(csv_filename, table_data):
    assert main.read_csv(csv_filename) == table_data


@pytest.mark.parametrize(
        'raw, header, value, op', [
            ('brand=apple', 'brand', 'apple', '='),
            ('price>149', 'price', '149', '>'),
            ('rating=avg', 'rating', 'avg', '='),
        ]
)
def test_clean_data(table_data, raw, header, value, op):
    headers = table_data[0].keys()
    assert main.clean_data(raw, headers) == (header, value, op)
    assert main.clean_data('name149', headers) is None


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

            ('price', '100', '<',
             []),
        ]
)
def test_filter_table(table_data, header, value, op, result):
    assert main.filter_table(table_data, header, value, op) == result


@pytest.mark.parametrize(
        'header, value, result', [
            ('price', 'max', [{'price': 1199.0}]),
            ('rating', 'min', [{'rating': 4.1}]),
            ('rating', 'avg', [{'rating': 4.49}])
        ]
)
def test_aggregate_table(table_data, header, value, result):
    assert main.aggregate_table(table_data, header, value) == result