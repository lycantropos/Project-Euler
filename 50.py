import operator
from functools import partial
from itertools import accumulate
from typing import (Iterable,
                    List)

from utils import prime_numbers


def consecutive_prime_numbers_decompositions(stop: int
                                             ) -> Iterable[List[int]]:
    numbers = list(prime_numbers(stop))
    # set lookups are faster than list ones
    numbers_set = set(numbers)

    stop_cube_root = int(stop ** (1 / 3))
    for position in range(len(numbers)):
        numbers_sublist = numbers[position:]
        numbers_sums = filter(partial(operator.ge, stop),
                              accumulate(numbers_sublist))
        sequence_length = 0
        for index, numbers_sum in enumerate(numbers_sums,
                                            start=1):
            if numbers_sum in numbers_set:
                sequence_length = index

        # TODO: find explanation for this heuristic
        if sequence_length < stop_cube_root:
            break

        if sequence_length > 1:
            yield numbers_sublist[:sequence_length]


def consecutive_prime_sum(stop: int) -> int:
    return sum(max(consecutive_prime_numbers_decompositions(stop),
                   key=len))


assert consecutive_prime_sum(100) == 41
assert consecutive_prime_sum(1_000) == 953
assert consecutive_prime_sum(1_000_000) == 997_651
