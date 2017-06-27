from typing import Iterable

from utils import proper_divisors


def amicable(number: int) -> bool:
    candidate = sum(proper_divisors(number))
    return (sum(proper_divisors(candidate)) == number and
            candidate != number)


def amicable_numbers(numbers: Iterable[int]) -> Iterable[int]:
    yield from filter(amicable, numbers)


assert amicable(220)
assert sum(amicable_numbers(range(1, 10_000))) == 31_626
