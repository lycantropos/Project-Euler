from functools import partial
from itertools import (count,
                       filterfalse)
from typing import Iterable

from utils import (max_number,
                   number_to_digits)


def exists_digits_powers_sum_number(digits_count: int,
                                    *,
                                    exponent: int) -> bool:
    return 9 ** (exponent + 1) * digits_count >= max_number(digits_count)


def max_digits_powers_sum_digits_count(exponent: int) -> int:
    return next(filterfalse(partial(exists_digits_powers_sum_number,
                                    exponent=exponent),
                            count(1)))


def digit_powers(exponent: int) -> Iterable[int]:
    def is_digits_powers_sum(number: int) -> bool:
        return sum(digit ** exponent
                   for digit in number_to_digits(number)) == number

    digits_count = max_digits_powers_sum_digits_count(exponent)
    stop = 10 ** digits_count
    yield from filter(is_digits_powers_sum, range(2, stop))


assert sum(digit_powers(4)) == 19_316
assert sum(digit_powers(5)) == 443_839
