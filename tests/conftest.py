import csv

import pytest


@pytest.fixture
def csv_filename():
    """Cодержит имя тестового csv файла."""
    return "./tests/test_data.csv"


@pytest.fixture
def table_data(csv_filename):
    """Считывает тестовый файл и преобразует в список словарей."""

    with open(csv_filename, 'r', encoding='utf-8') as f:
        file_reader = csv.DictReader(f)
        return list(file_reader)
