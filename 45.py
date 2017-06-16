from itertools import count
from typing import Iterator

from utils import (triangular,
                   pentagonial)


def hexagonal_number(index: int) -> int:
    return index * (2 * index - 1)


def triangular_pentagonal_hexagonal_numbers(start: int) -> Iterator[int]:
    hexagonal_numbers = map(hexagonal_number, count(start))
    triangular_hexagonal_numbers = filter(triangular, hexagonal_numbers)
    yield from filter(pentagonial, triangular_hexagonal_numbers)


numbers_generator = triangular_pentagonal_hexagonal_numbers(1)

assert next(numbers_generator) == 1
assert next(numbers_generator) == 40_755
assert next(numbers_generator) == 1_533_776_805
