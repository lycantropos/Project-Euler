from itertools import (count,
                       chain)
from typing import (Iterable,
                    Set)

from utils import max_factor

concatenate_iterables = chain.from_iterable


def factors(number: int) -> Set[int]:
    return set(concatenate_iterables((factor, number // factor)
                                     for factor in range(1, max_factor(number) + 1)
                                     if number % factor == 0))


def triangle_numbers() -> Iterable[int]:
    for index in count(1):
        yield index * (index + 1) // 2


def highly_divisible_triangular_number(factors_count: int) -> int:
    return next(number
                for number in triangle_numbers()
                if len(factors(number)) >= factors_count)


assert highly_divisible_triangular_number(factors_count=500) == 76_576_500
