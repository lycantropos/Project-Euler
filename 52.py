from itertools import count
from typing import Iterator

from utils import number_to_digits


def permuted_multiples(max_multiplier: int) -> Iterator[int]:
    for number in count(1):
        sorted_digits = sorted(number_to_digits(number))
        for multiplier in range(2, max_multiplier + 1):
            multiplied_number = multiplier * number
            if sorted(number_to_digits(multiplied_number)) != sorted_digits:
                break
        else:
            yield number


assert next(permuted_multiples(2)) == 125_874
assert next(permuted_multiples(6)) == 142_857
