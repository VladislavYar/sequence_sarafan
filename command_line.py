from argparse import ArgumentParser, ArgumentTypeError


def validate_positive_number(value):
    """Валидация введённого числа на положительность."""
    value = int(value)
    if value < 0:
        raise ArgumentTypeError(
            f'value is an invalid positive int value: {value}'
            )
    return value


def parser_command_line() -> ArgumentParser:
    """Парсер командной строки."""
    parser = ArgumentParser(description='Вывод последовательности чисел')
    parser.add_argument(
        '-c',
        '--count',
        type=validate_positive_number,
        help='кол-во элементов в последовательности'
    )
    return parser
