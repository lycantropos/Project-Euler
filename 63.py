import operator
from itertools import (count,
                       product,
                       starmap)
from typing import (Iterable,
                    Tuple)

from utils import number_digits_count


def max_digits_count() -> int:
    for exponent in count(1):
        # exponent grows faster than digits count
        # for powers with base 10 or greater
        if number_digits_count(9 ** exponent) < exponent:
            return exponent


def digits_counts_exponents(bases: Iterable[int],
                            exponents: Iterable[int]
                            ) -> Iterable[Tuple[int, int]]:
    for base, exponent in product(bases, exponents):
        yield number_digits_count(base ** exponent), exponent


def powerful_digit_counts(bases: Iterable[int],
                          exponents: Iterable[int]) -> int:
    return sum(starmap(operator.eq,
                       digits_counts_exponents(
                           bases=bases,
                           exponents=exponents)))


assert powerful_digit_counts(bases=range(1, 10),
                             exponents=range(1, max_digits_count())) == 49
