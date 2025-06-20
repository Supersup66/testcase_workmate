class NoOperand(Exception):
    """Отсутствует необходимый операнд."""


class HeaderError(Exception):
    """Ошибка в имени заголовка."""


class ResponseStatusError(Exception):
    """Сервер вернул статус отличный от 200."""