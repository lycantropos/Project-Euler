from functools import partial
from itertools import filterfalse

from utils import (is_perfect_square,
                   odd,
                   sqrt_continued_fraction_period)


def odd_period_square_roots(*,
                            start: int = 1,
                            stop: int,
                            step: int = 1,
                            members_count_start: int = 250,
                            members_count_step: int = 50,
                            precision_start: int = 500,
                            precision_step: int = 250,
                            precision_stop: int = 2_501) -> int:
    numbers = range(start, stop, step)
    numbers = filterfalse(is_perfect_square, numbers)
    number_period = partial(sqrt_continued_fraction_period,
                            members_count_start=members_count_start,
                            members_count_step=members_count_step,
                            precision_start=precision_start,
                            precision_step=precision_step,
                            precision_stop=precision_stop)
    cycles_lengths = map(len, map(number_period, numbers))
    return sum(map(odd, cycles_lengths))


assert odd_period_square_roots(stop=14) == 4
assert odd_period_square_roots(stop=10_001) == 1_322
