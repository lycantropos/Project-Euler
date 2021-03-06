from fractions import Fraction

from utils import reduced_proper_fractions

stop_fraction = Fraction(3, 7)

assert max(reduced_proper_fractions(stop=stop_fraction,
                                    max_denominator=8,
                                    only_first=True)
           ) == Fraction(2, 5)
assert max(reduced_proper_fractions(stop=stop_fraction,
                                    max_denominator=1_000_000,
                                    only_first=True)
           ) == Fraction(428_570, 999_997)
