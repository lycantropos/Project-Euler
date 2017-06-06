import operator
from functools import (partial,
                       reduce)
from math import sqrt
from typing import (Any,
                    Iterable,
                    Sequence)

multiply = partial(reduce, operator.mul)


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
