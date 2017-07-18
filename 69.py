from fractions import Fraction

from utils import (prime,
                   factors,
                   multiply)


def n_phi(number: int) -> Fraction:
    # based on
    # https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler.27s_product_formula
    prime_factors = filter(prime, factors(number))
    numerators, denominators = zip(*((factor, factor - 1)
                                     for factor in prime_factors))
    return Fraction(multiply(numerators),
                    multiply(denominators))


example_totient_maximum_argument = max(range(2, 11),
                                       key=n_phi)
totient_maximum_argument = max(range(2, 1_000_001),
                               key=n_phi)

assert example_totient_maximum_argument == 6
assert totient_maximum_argument == 510_510
