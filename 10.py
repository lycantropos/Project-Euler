from math import sqrt
from typing import List


def primes(number: int) -> List[int]:
    # based on
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    number_mod_six = number % 6
    correction = number_mod_six > 1
    number = {0: number,
              1: number - 1,
              2: number + 4,
              3: number + 3,
              4: number + 2,
              5: number + 1}[number_mod_six]
    number_third_part = number // 3
    sieve = [True] * number_third_part
    sieve[0] = False
    factor_stop = int(sqrt(number)) // 3 + 1
    for factor in range(factor_stop):
        if not sieve[factor]:
            continue

        k = 3 * factor + 1 | 1
        k_squared = k * k
        k_doubled = 2 * k
        number_sixth_part_pred = number // 6 - 1
        sieve[(k_squared // 3)::k_doubled] = (
            [False]
            * ((number_sixth_part_pred - k_squared // 6) // k + 1))

        k_diff = k_squared + 4 * k - k_doubled * (factor & 1)
        sieve[k_diff // 3::k_doubled] = (
            [False]
            * ((number_sixth_part_pred - k_diff // 6) // k + 1))

    yield 2
    yield 3
    yield from (3 * i + 1 | 1
                for i in range(1, number_third_part - correction)
                if sieve[i])


def sum_of_primes(stop: int) -> int:
    return sum(primes(stop))


assert sum_of_primes(10) == 17
assert sum_of_primes(2_000_000) == 142_913_828_922
