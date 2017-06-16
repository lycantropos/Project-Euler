from utils import (primes,
                   digits_to_number,
                   number_to_digits)

pandigits = {digit: set(range(1, digit + 1))
             for digit in range(1, 10)}


def is_pandigital(number: int) -> bool:
    digits = list(number_to_digits(number))
    digits_set = set(digits)
    if len(digits) > len(digits_set):
        return False
    max_digit = max(digits_set)
    return not (pandigits[max_digit] ^ digits_set)


pandigital_primes = filter(is_pandigital,
                           # 9-digit pandigital prime doesn't exist
                           # since
                           # 1 + 2 + ... + 9 = 45
                           # => it will be always divided by 3 and 9
                           primes(digits_to_number(range(8, 0, -1)),
                                  reverse=True))
assert next(pandigital_primes) == 7_652_413
