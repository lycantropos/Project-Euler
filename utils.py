import operator
from functools import (partial,
                       reduce)
from itertools import chain
from math import sqrt
from typing import (Any,
                    Iterable,
                    Sequence,
                    Set)

multiply = partial(reduce, operator.mul)

concatenate_iterables = chain.from_iterable


def chunks(elements: Sequence[Any],
           size: int) -> Iterable[Sequence[Any]]:
    elements_count = len(elements)
    for offset in range(elements_count):
        yield elements[offset:offset + size]


def max_factor(number: int) -> int:
    return int(sqrt(number))


def even(number: int) -> bool:
    return number % 2 == 0


def sum_of_digits(number: int) -> int:
    return sum(map(int, str(number)))


def factors(number: int,
            *,
            start: int = 1) -> Set[int]:
    return set(
        chain([1],
              concatenate_iterables(
                  (factor, number // factor)
                  for factor in range(start, max_factor(number) + 1)
                  if number % factor == 0)))


proper_divisors = partial(factors,
                          start=2)
