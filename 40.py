from utils import (multiply,
                   max_number)


def champernowne_constant(exponent: int = 6) -> int:
    digits_count = 0
    length = 0
    while length < 10 ** exponent:
        digits_count += 1
        length += digits_count * 9 * 10 ** (digits_count - 1)
    stop = max_number(digits_count)
    fractional_part = ''.join(map(str, range(1, stop)))
    return multiply(int(fractional_part[10 ** exponent - 1])
                    for exponent in range(exponent + 1))


assert champernowne_constant() == 210
