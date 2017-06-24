from typing import Tuple

from utils import (multiply,
                   pythagorean_triplets)

numbers_sum = 1_000


def special_condition(numbers: Tuple[int, ...]) -> bool:
    return sum(numbers) == numbers_sum


special_pythagorean_triplet, = filter(special_condition,
                                      pythagorean_triplets(numbers_sum))

assert multiply(special_pythagorean_triplet) == 31_875_000
