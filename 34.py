from itertools import (count,
                       filterfalse)
from math import factorial
from typing import Iterable

from utils import number_to_digits

digits_factorials = {digit: factorial(digit)
                     for digit in range(10)}


def exists_digits_factorials_sum_number(digits_count: int) -> bool:
    return digits_factorials[9] * digits_count * 9 >= 10 ** digits_count - 1


def max_digits_factorials_sum_digits_count() -> int:
    return next(filterfalse(exists_digits_factorials_sum_number,
                            count(1)))


def digit_factorials(*,
                     step: int = 1) -> Iterable[int]:
    digits_count = max_digits_factorials_sum_digits_count()
    stop = 10 ** digits_count
    candidates = filter(is_digits_factorials_sum_candidate,
                        range(3, stop, step))
    yield from filter(is_digits_factorials_sum,
                      candidates)


def is_digits_factorials_sum(number: int) -> bool:
    digits_factorials_sum = sum(digits_factorials[digit]
                                for digit in number_to_digits(number))
    return digits_factorials_sum == number


def is_digits_factorials_sum_candidate(number: int) -> bool:
    digits = tuple(number_to_digits(number))
    zeros_count = digits.count(0)
    ones_count = digits.count(1)
    last_digit = digits[-1]
    return last_digit % 2 == (zeros_count + ones_count) % 2


assert is_digits_factorials_sum(145)
assert sum(digit_factorials()) == 40_730
