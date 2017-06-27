import operator
from collections import Counter
from functools import reduce
from itertools import starmap
from typing import Iterable


def prime_factors(number: int) -> Iterable[int]:
    factor = 2
    while factor * factor <= number:
        if number % factor:
            factor += 1
        else:
            yield factor
            number //= factor
    yield number


def evenly_divisible(numbers: Iterable[int]) -> int:
    divisors = Counter()
    for number in numbers:
        factors_counter = Counter(prime_factors(number))
        for key, value in factors_counter.items():
            divisors[key] = max(divisors[key], value)
    return reduce(operator.mul, starmap(pow, divisors.items()))


assert evenly_divisible(range(1, 10)) == 2520
assert evenly_divisible(range(1, 20)) == 232_792_560
