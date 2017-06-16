from itertools import (count,
                       islice)

from utils import prime


def prime_number_by_index(index: int) -> int:
    prime_numbers = filter(prime, count(1))
    res, = islice(prime_numbers, index - 1, index)
    return res


assert prime_number_by_index(6) == 13
assert prime_number_by_index(10_001) == 104_743
