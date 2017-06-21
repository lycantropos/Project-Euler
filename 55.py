from utils import (number_to_digits,
                   digits_to_number,
                   is_palindrome,
                   capacity)

MAX_ITERATIONS_COUNT = 50


def lychrel(number: int) -> bool:
    for _ in range(MAX_ITERATIONS_COUNT):
        number += digits_to_number(reversed(list(number_to_digits(number))))
        if is_palindrome(str(number)):
            return False
    return True


assert not lychrel(47)
assert not lychrel(349)
assert lychrel(196)
assert capacity(filter(lychrel, range(1, 10_000))) == 249
