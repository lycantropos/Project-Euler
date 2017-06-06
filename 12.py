from itertools import count
from typing import Iterable

from utils import factors


def triangle_numbers() -> Iterable[int]:
    for index in count(1):
        yield index * (index + 1) // 2


def factors_count(number: int) -> int:
    return len(factors(number))


def highly_divisible_triangular_number(*,
                                       target_factors_count: int
                                       ) -> int:
    return next(number
                for number in triangle_numbers()
                if factors_count(number) >= target_factors_count)


assert highly_divisible_triangular_number(target_factors_count=500) == 76_576_500
