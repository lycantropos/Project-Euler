from itertools import product
from typing import Iterable


def powers(*,
           base_start: int,
           base_stop: int,
           base_step: int = 1,
           exponent_start: int,
           exponent_stop: int,
           exponent_step: int = 1) -> Iterable[int]:
    bases = range(base_start, base_stop, base_step)
    exponents = range(exponent_start, exponent_stop, exponent_step)
    bases_exponents = product(bases, exponents)
    for base, exponent in bases_exponents:
        yield base ** exponent


def distinct_powers(*,
                    base_start: int,
                    base_stop: int,
                    base_step: int = 1,
                    exponent_start: int,
                    exponent_stop: int,
                    exponent_step: int = 1) -> int:
    return len(set(powers(base_start=base_start,
                          base_stop=base_stop,
                          base_step=base_step,
                          exponent_start=exponent_start,
                          exponent_stop=exponent_stop,
                          exponent_step=exponent_step)))


assert distinct_powers(base_start=2,
                       base_stop=6,
                       exponent_start=2,
                       exponent_stop=6) == 15
assert distinct_powers(base_start=2,
                       base_stop=101,
                       exponent_start=2,
                       exponent_stop=101) == 9_183
