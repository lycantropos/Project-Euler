from functools import partial
from math import factorial
from typing import List

from utils import (number_to_digits,
                   has_n_elements)


def digits_factorials_chain(number: int) -> List[int]:
    chain = [number]
    while True:
        digits = number_to_digits(number)
        digits_factorials = map(factorial, digits)
        digits_factorials_sum = sum(digits_factorials)
        if digits_factorials_sum in chain:
            break
        number = digits_factorials_sum
        chain.append(number)
    return chain


digits_factorials_chains = map(digits_factorials_chain,
                               range(1, 1_000_000))
has_sixty_elements = partial(has_n_elements,
                             n=60)

assert digits_factorials_chain(145) == [145]
assert digits_factorials_chain(169) == [169, 363_601, 1_454]
assert digits_factorials_chain(871) == [871, 45_361]
assert digits_factorials_chain(872) == [872, 45_362]
assert digits_factorials_chain(69) == [69, 363_600, 1454, 169, 363_601]
assert digits_factorials_chain(78) == [78, 45_360, 871, 45_361]
assert digits_factorials_chain(540) == [540, 145]
assert sum(map(has_sixty_elements, digits_factorials_chains)) == 402
