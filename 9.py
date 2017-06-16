from typing import Tuple

from utils import (multiply,
                   pythagorean_triplets_candidates,
                   is_pythagorean_triplet)

numbers_sum = 1_000


def special_condition(numbers: Tuple[int, ...]) -> bool:
    return sum(numbers) == numbers_sum


special_pythagorean_triplet, = filter(is_pythagorean_triplet,
                                      filter(special_condition,
                                             set(pythagorean_triplets_candidates(
                                                 numbers_sum))))

assert multiply(special_pythagorean_triplet) == 31_875_000
