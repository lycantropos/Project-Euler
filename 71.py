from fractions import Fraction
from math import gcd
from typing import Iterable


def relatively_prime(number: int, other_number: int) -> bool:
    return gcd(number, other_number) == 1


def reduced_proper_fractions(stop: Fraction,
                             max_denominator: int) -> Iterable[Fraction]:
    stop_numerator, stop_denominator = stop.numerator, stop.denominator
    stop_float = float(stop)
    for denominator in range(max_denominator, 1, -1):
        for numerator in range(int(stop_float * denominator), 0, -1):
            if stop_denominator * numerator >= stop_numerator * denominator:
                continue
            if not relatively_prime(numerator, denominator):
                continue
            yield Fraction(numerator, denominator)
            break


stop_fraction = Fraction(3, 7)

assert max(reduced_proper_fractions(stop=stop_fraction,
                                    max_denominator=8)
           ) == Fraction(2, 5)
assert max(reduced_proper_fractions(stop=stop_fraction,
                                    max_denominator=1_000_000)
           ) == Fraction(428_570, 999_997)
