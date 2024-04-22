

def get_sequence(max_count: int) -> str:
    """Возвращает строковую последовательность чисел."""
    number = 0
    sequence = []
    while max_count > 0:
        number += 1
        count = number
        if count > max_count:
            count = max_count
        max_count -= count
        sequence.append(str(number) * count)
    return str.join('', sequence)
