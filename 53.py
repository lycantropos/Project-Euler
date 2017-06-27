import operator
from functools import partial
from itertools import product
from typing import Iterable

from utils import (binomial_coefficient,
                   capacity)


def combinatoric_selections(numbers: Iterable[int]) -> Iterable[int]:
    for n, k in product(numbers, repeat=2):
        yield binomial_coefficient(n, k)


values_greater_than_one_million = filter(partial(operator.lt, 1_000_000),
                                         combinatoric_selections(range(1,
                                                                       101)))

assert binomial_coefficient(5, 3) == 10
assert binomial_coefficient(23, 10) == 1_144_066
assert capacity(values_greater_than_one_million) == 4_075
