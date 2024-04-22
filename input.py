

def input_number() -> int:
    """
    Возвращает введённое пользователем целое положительное число.
    """
    number = ''
    while not number.isdigit():
        number = input('Введите целое число: ')
    return int(number)
