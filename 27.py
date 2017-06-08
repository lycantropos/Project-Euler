from itertools import (product,
                       count)
from typing import Tuple

from utils import (primes,
                   is_prime,
                   multiply)


def consecutive_quadratic_primes_count(coefficients: Tuple[int, int]
                                       ) -> int:
    linear_coefficient, constant_term = coefficients

    def quadratic_formula(n: int) -> int:
        return n ** 2 + linear_coefficient * n + constant_term

    for number in count(0):
        value = quadratic_formula(number)
        if value < 0 or not is_prime(value):
            return number


def max_consecutive_primes_count_coefficients(stop: int) -> Tuple[int, int]:
    formulas_coefficients = product(range(-stop, stop),
                                    primes(stop + 1))
    return max(formulas_coefficients,
               key=consecutive_quadratic_primes_count)


assert consecutive_quadratic_primes_count((1, 41)) == 40
assert consecutive_quadratic_primes_count((-79, 1_601)) == 80
assert multiply(max_consecutive_primes_count_coefficients(1_000)) == -59_231
