from typing import Iterable

from utils import (phi,
                   n_phi)


def are_permutations(iterable: Iterable,
                     other_iterable: Iterable) -> bool:
    return sorted(iterable) == sorted(other_iterable)


def totient_permutations(numbers: Iterable[int]) -> Iterable[int]:
    totients = map(phi, numbers)
    for number, totient in zip(numbers, totients):
        if are_permutations(str(number), str(totient)):
            yield number


assert min(totient_permutations(range(10_000_000 - 1, 1, -1)),
           key=n_phi) == 8_319_823
