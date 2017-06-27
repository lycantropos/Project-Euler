from fractions import Fraction
from typing import Iterable

from utils import (number_to_digits,
                   capacity)


def square_root_expansions(stop: int) -> Iterable[Fraction]:
    result = Fraction(3, 2)
    yield result
    for index in range(stop):
        result = Fraction(1) + Fraction(1, 1 + result)
        yield result


def square_root_convergents(stop: int) -> Iterable[bool]:
    for expansion in square_root_expansions(stop):
        numerator_digits_count = capacity(number_to_digits(expansion
                                                           .numerator))
        denominator_digits_count = capacity(number_to_digits(expansion
                                                             .denominator))
        yield numerator_digits_count > denominator_digits_count


assert sum(square_root_convergents(1_001)) == 153
