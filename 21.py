from typing import Iterable

from utils import proper_divisors


def amicable(number: int) -> bool:
    candidate = sum(proper_divisors(number))
    return (sum(proper_divisors(candidate)) == number and
            candidate != number)


def amicable_numbers(*,
                     start: int = 1,
                     stop: int,
                     step: int = 1) -> Iterable[int]:
    yield from filter(amicable, range(start, stop, step))


assert amicable(220)
assert sum(amicable_numbers(stop=10_000)) == 31_626
