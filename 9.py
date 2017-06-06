from itertools import permutations
from typing import Tuple

from utils import (multiply,
                   max_factor)

MAX_NUMBER = 1000

MIN_N = 1
MIN_M = 2


def pythagorean_triples_candidates(*,
                                   stop: int):
    # based on
    # https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    max_k = stop // (MIN_N ** 2 + MIN_M ** 2)
    for k in range(1, max_k + 1):
        numbers = range(1, max_factor(stop // k))
        for n, m in map(sorted, permutations(numbers, r=2)):
            candidate = sorted([m ** 2 - n ** 2,
                                2 * m * n,
                                m ** 2 + n ** 2])
            yield tuple(k * coordinate
                        for coordinate in candidate)


def is_pythagorean_triple(numbers: Tuple[int, int, int]) -> bool:
    a, b, c = numbers
    return a ** 2 + b ** 2 == c ** 2


def special_condition(numbers: Tuple[int, ...]) -> bool:
    return sum(numbers) == MAX_NUMBER


special_pythagorean_triplet, = filter(is_pythagorean_triple,
                                      filter(special_condition,
                                             set(pythagorean_triples_candidates(
                                                 stop=MAX_NUMBER))))

assert multiply(special_pythagorean_triplet) == 31_875_000
