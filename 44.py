from itertools import count
from typing import Optional

from utils import (is_perfect_square,
                   int_sqrt)


def pentagonial_number(index: int) -> int:
    return index * (3 * index - 1) // 2


def positive_root(constant_term: int) -> Optional[int]:
    discriminant = 1 + 24 * constant_term
    if is_perfect_square(discriminant):
        numerator = 1 + int_sqrt(discriminant)
        if numerator % 6:
            return
        return numerator // 6


# TODO: improve this "bruteforcefully" working function
def pentagon_numbers(offset: int) -> int:
    for j in count(1):
        p_j = pentagonial_number(j)
        for s in range(j + 1, j + offset):
            p_s = pentagonial_number(s)
            p_k = p_s - p_j
            p_d = p_k - p_j

            k = positive_root(p_k)
            if k is None:
                continue

            try:
                d = positive_root(p_d)
            except ValueError:
                continue
            if d is None:
                continue

            break
        else:
            continue

        return p_k - p_j


assert pentagon_numbers(offset=10_000) == 5_482_660
