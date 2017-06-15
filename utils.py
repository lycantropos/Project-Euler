import operator
from functools import (partial,
                       reduce)
from itertools import chain
from math import sqrt
from numbers import Real
from typing import (Any,
                    Iterable,
                    Sequence,
                    Set,
                    List)

multiply = partial(reduce, operator.mul)

concatenate_iterables = chain.from_iterable


def chunks(elements: Sequence[Any],
           size: int) -> Iterable[Sequence[Any]]:
    elements_count = len(elements)
    for offset in range(elements_count):
        yield elements[offset:offset + size]


def max_factor(number: int) -> int:
    return int(sqrt(number))


def odd(number: int) -> int:
    return number & 1


def digits_sum(number: int) -> int:
    return sum(number_to_digits(number))


def number_to_digits(number: int) -> Iterable[int]:
    yield from map(int, str(number))


def digits_to_number(digits: Iterable[int]) -> int:
    return int(''.join(map(str, digits)))


def factors(number: int,
            *,
            start: int = 1) -> Set[int]:
    return set(
        chain([1],
              concatenate_iterables(
                  (factor, number // factor)
                  for factor in range(start, max_factor(number) + 1)
                  if number % factor == 0)))


proper_divisors = partial(factors,
                          start=2)


def fibonacci(stop: Real = float('inf')) -> Iterable[int]:
    a, b = 0, 1
    while b < stop:
        yield b
        a, b = b, a + b


def primes(number: int) -> List[int]:
    # based on
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    yield 2
    yield 3
    if number < 5:
        return
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
    factor_stop = max_factor(number) // 3 + 1
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

    yield from (3 * i + 1 | 1
                for i in range(1, number_third_part - correction)
                if sieve[i])


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
