import operator
from functools import partial
from itertools import product

from utils import (binomial_coefficient,
                   capacity)


def combinatoric_selections(*,
                            start: int = 1,
                            stop: int,
                            step: int = 1
                            ):
    for n, k in product(range(start, stop, step), repeat=2):
        yield binomial_coefficient(n, k)


values_greater_than_one_million = filter(partial(operator.lt, 1_000_000),
                                         combinatoric_selections(stop=101))

assert binomial_coefficient(5, 3) == 10
assert binomial_coefficient(23, 10) == 1_144_066
assert capacity(values_greater_than_one_million) == 4_075
