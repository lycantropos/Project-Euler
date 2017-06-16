from itertools import permutations
from math import ceil
from typing import (Iterator,
                    Collection)

from utils import (digits_to_number,
                   number_to_digits)


def pandigital_multiples(digits: Collection[int]) -> Iterator[int]:
    position_stop = ceil(len(digits) / 2)
    for digits in permutations(digits):
        for position in range(1, position_stop):
            base_digits = digits[:position]
            base = digits_to_number(base_digits)
            base_digits_set = set(base_digits)
            tail_start = position
            for multiplier in range(2, 10):
                tail = ''.join(map(str, digits[tail_start:]))
                if not tail:
                    continue
                step = base * multiplier
                step_digits = list(number_to_digits(step))
                step_digits_set = set(step_digits)
                step_digits_count = len(step_digits)
                if step_digits_count < len(step_digits_set):
                    break
                if step_digits_set & base_digits_set:
                    break
                if not tail.startswith(str(step)):
                    break
                tail_start += step_digits_count
            else:
                yield digits_to_number(digits)


assert next(pandigital_multiples(range(9, 0, -1))) == 932_718_654
