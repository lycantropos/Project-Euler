from itertools import (filterfalse,
                       product)
from typing import Iterable

from utils import number_to_digits


def ends_with_zero(number: int) -> bool:
    return str(number).endswith('0')


def digits_sums(*,
                start: int = 1,
                stop: int,
                step: int = 1) -> Iterable[int]:
    if stop == 2:
        return 1,
    bases = filterfalse(ends_with_zero,
                        range(start, stop, step))
    exponents = range(2, stop)
    for base, exponent in product(bases, exponents):
        yield sum(number_to_digits(base ** exponent))


assert max(digits_sums(stop=100)) == 972
