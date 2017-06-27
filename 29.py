from itertools import product
from typing import Iterable


def powers(*,
           bases: Iterable[int],
           exponents: Iterable[int]) -> Iterable[int]:
    bases_exponents = product(bases, exponents)
    for base, exponent in bases_exponents:
        yield base ** exponent


def distinct_powers(*,
                    bases: Iterable[int],
                    exponents: Iterable[int]) -> int:
    return len(set(powers(bases=bases,
                          exponents=exponents)))


assert distinct_powers(bases=range(2, 6),
                       exponents=range(2, 6)) == 15
assert distinct_powers(bases=range(2, 101),
                       exponents=range(2, 101)) == 9_183
