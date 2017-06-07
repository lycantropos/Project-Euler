import operator
from collections import OrderedDict
from functools import partial
from itertools import (takewhile,
                       filterfalse,
                       zip_longest)
from typing import Iterable

from utils import proper_divisors


def is_abundant(number: int) -> bool:
    return sum(proper_divisors(number)) > number


def non_abundant_numbers_sum(*,
                             start: int = 1,
                             stop: int,
                             step: int = 1
                             ) -> Iterable[int]:
    numbers = range(2, stop)
    target_abundant_numbers = OrderedDict(zip_longest(filter(is_abundant,
                                                             numbers),
                                                      []))

    def is_abundant_numbers_sum(number: int) -> bool:
        lesser_abundant_numbers = takewhile(partial(operator.ge, number),
                                            target_abundant_numbers)
        for abundant_number in lesser_abundant_numbers:
            try:
                target_abundant_numbers[number - abundant_number]
            except KeyError:
                continue
            else:
                return True
        return False

    return filterfalse(is_abundant_numbers_sum,
                       range(start, stop, step))


assert all(not is_abundant(number)
           for number in range(1, 12))
assert is_abundant(12)
assert 24 not in list(non_abundant_numbers_sum(stop=25))
assert sum(non_abundant_numbers_sum(stop=28_124)) == 4_179_871
