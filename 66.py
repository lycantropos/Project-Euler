from itertools import (filterfalse,
                       count)
from operator import itemgetter
from typing import (Iterable,
                    Tuple)

from utils import (is_perfect_square,
                   sqrt_convergent)


def fundamental_solutions(coefficients: Iterable[int]
                          ) -> Iterable[Tuple[int, Tuple[int, int]]]:
    coefficients = filterfalse(is_perfect_square, coefficients)
    for coefficient in coefficients:
        for index in count():
            convergent = sqrt_convergent(coefficient, index)
            left_term, right_term = (convergent.numerator,
                                     convergent.denominator)
            if left_term ** 2 - coefficient * right_term ** 2 == 1:
                yield coefficient, (left_term, right_term)
                break


maximin_coefficient_leq_seven, _ = max(fundamental_solutions(range(8)),
                                       key=itemgetter(1))
maximin_coefficient_leq_thousand, _ = max(fundamental_solutions(range(1_000)),
                                          key=itemgetter(1))

assert maximin_coefficient_leq_seven == 5
assert maximin_coefficient_leq_thousand == 661
