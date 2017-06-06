from typing import Iterable

from utils import factors


def is_amicable_number(number: int):
    candidate = sum(factors(number, start=2))
    return (sum(factors(candidate, start=2)) == number and
            candidate != number)


def amicable_numbers(*,
                     start: int = 1,
                     stop: int,
                     step: int = 1) -> Iterable[int]:
    yield from filter(is_amicable_number, range(start, stop, step))


assert is_amicable_number(220)
assert sum(amicable_numbers(stop=10_000)) == 31_626
