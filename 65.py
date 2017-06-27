from fractions import Fraction
from itertools import (count,
                       islice)
from typing import Iterable

from utils import number_to_digits


def continued_fraction() -> Iterable[int]:
    yield 2
    for index in count(1):
        yield 1
        yield 2 * index
        yield 1


def convergent(index: int) -> Fraction:
    coefficients = list(islice(continued_fraction(), index))
    # we are starting from the bottom to the top
    result = Fraction(coefficients.pop())
    for coefficient in reversed(coefficients):
        result = coefficient + Fraction(1, result)
    return result


assert [convergent(index)
        for index in range(1, 11)] == [Fraction(2),
                                       Fraction(3),
                                       Fraction(8, 3),
                                       Fraction(11, 4),
                                       Fraction(19, 7),
                                       Fraction(87, 32),
                                       Fraction(106, 39),
                                       Fraction(193, 71),
                                       Fraction(1264, 465),
                                       Fraction(1457, 536)]
assert sum(number_to_digits(convergent(10).numerator)) == 17
assert sum(number_to_digits(convergent(100).numerator)) == 272
