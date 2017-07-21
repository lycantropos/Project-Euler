from fractions import Fraction

from utils import (reduced_proper_fractions,
                   capacity)

assert capacity(reduced_proper_fractions(start=Fraction(1, 3),
                                         stop=Fraction(1, 2),
                                         max_denominator=12_000)) == 7_295_372
