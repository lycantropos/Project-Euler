import operator
from functools import partial
from typing import (Iterable,
                    Tuple)

from utils import (prime_numbers,
                   number_to_digits)


def prime_permutations(*,
                       start: int,
                       stop: int,
                       increment: int) -> Iterable[Tuple[int, int, int]]:
    prime_numbers_set = set(filter(partial(operator.le, start),
                                   prime_numbers(stop)))
    for number in filter(partial(operator.ge, 10_000 - increment * 2),
                         prime_numbers_set):
        sorted_digits = sorted(number_to_digits(number))
        second_number = number + increment
        third_number = second_number + increment
        second_number_digits = sorted(number_to_digits(second_number))
        third_number_digits = sorted(number_to_digits(third_number))
        if sorted_digits == second_number_digits == third_number_digits:
            if second_number in prime_numbers_set and third_number in prime_numbers_set:
                yield number, second_number, third_number


sequences = list(prime_permutations(start=1_000,
                                    stop=10_000,
                                    increment=3_330))

assert (1487, 4817, 8147) in sequences
assert len(sequences) == 2
assert (2969, 6299, 9629) in sequences
