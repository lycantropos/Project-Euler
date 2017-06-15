from fractions import Fraction
from itertools import permutations
from typing import (Iterable,
                    Tuple)

from utils import (multiply,
                   number_to_digits,
                   digits_to_number)


def curious_fractions(*,
                      start: int,
                      stop: int,
                      step: int = 1
                      ) -> Iterable[Fraction]:
    numbers = range(start, stop, step)
    fractions_parts = permutations(numbers, r=2)
    filtered_fractions_parts = filter(non_trivial_fraction,
                                      filter(less_than_one_in_value,
                                             fractions_parts))
    for numerator, denominator in filtered_fractions_parts:
        numerator_digits = list(number_to_digits(numerator))
        denominator_digits = list(number_to_digits(denominator))
        try:
            common_digit, = set(numerator_digits) & set(denominator_digits)
        except ValueError:
            continue
        else:
            cancelled_numerator_digits = numerator_digits[:]
            cancelled_numerator_digits.remove(common_digit)

            cancelled_denominator_digits = denominator_digits[:]
            cancelled_denominator_digits.remove(common_digit)

            cancelled_numerator = digits_to_number(cancelled_numerator_digits)
            cancelled_denominator = digits_to_number(cancelled_denominator_digits)

            fraction = Fraction(numerator, denominator)
            cancelled_fraction = Fraction(cancelled_numerator,
                                          cancelled_denominator)
            fraction_is_curious = fraction == cancelled_fraction
            if fraction_is_curious:
                yield fraction


def less_than_one_in_value(fraction_parts: Tuple[int, int]) -> bool:
    numerator, denominator = fraction_parts
    return numerator < denominator


def non_trivial_fraction(fraction_parts: Tuple[int, int]) -> bool:
    numerator, denominator = fraction_parts
    return bool(numerator % 10 and denominator % 10)


assert multiply(curious_fractions(start=10,
                                  stop=100)).denominator == 100
