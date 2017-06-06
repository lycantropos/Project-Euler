from itertools import (count,
                       islice)

from utils import max_factor


def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number == 1 or number % 2 == 0:
        return False
    odd_factors = range(3, max_factor(number) + 1, 2)
    for factor in odd_factors:
        if number % factor == 0:
            return False
    return True


def prime_number_by_index(index: int) -> int:
    prime_numbers = filter(is_prime, count(1))
    res, = islice(prime_numbers, index - 1, index)
    return res


assert prime_number_by_index(6) == 13
assert prime_number_by_index(10_001) == 104_743
