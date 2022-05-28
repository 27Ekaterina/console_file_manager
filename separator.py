def separator(count=30):
    """
    Функция разделитель
    :param count: количество звездочек
    :return: красивый разделитель
    """
    return '*' * count

def add_separators(f):
    def inner(*args, **kwargs):
        print(separator())
        result = f(*args, **kwargs)
        print(separator())
        return result
    return inner