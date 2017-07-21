from itertools import chain
from typing import Iterable

from utils import (SPIRAL_START,
                   spiral_corners,
                   prime,
                   capacity)


def spiral_diagonal_numbers(dimension: int) -> Iterable[int]:
    yield from chain([SPIRAL_START],
                     chain.from_iterable(spiral_corners(dimension)))


def spiral_primes_ratio(dimension: int) -> float:
    diagonal_numbers = list(spiral_diagonal_numbers(dimension))
    diagonal_prime_numbers_count = capacity(filter(prime,
                                                   reversed(diagonal_numbers)))
    return diagonal_prime_numbers_count / len(diagonal_numbers)


def spiral_primes(*,
                  start: int = 3,
                  target_ratio: float,
                  step_exponent: int = 10) -> int:
    dimension = start
    step = 2 ** step_exponent
    while step > 2:
        dimension = suffice_dimension(start=dimension,
                                      step=step,
                                      target_ratio=target_ratio)
        reduced_dimension = dimension - step
        # for degenerate single-element spiral ratio equal to zero
        if reduced_dimension > SPIRAL_START:
            dimension = reduced_dimension
        step //= 2
    return suffice_dimension(start=dimension,
                             step=step,
                             target_ratio=target_ratio)


def suffice_dimension(*,
                      start: int,
                      step: int,
                      target_ratio: float) -> int:
    dimension = start
    ratio = spiral_primes_ratio(dimension)
    while ratio > target_ratio:
        dimension += step
        ratio = spiral_primes_ratio(dimension)
    return dimension


assert round(spiral_primes_ratio(7), 2) == 0.62
assert spiral_primes(target_ratio=0.1) == 26_241
