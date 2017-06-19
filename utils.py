import operator
from functools import (partial,
                       reduce)
from itertools import (chain,
                       permutations)
from math import sqrt, factorial
from numbers import Real
from typing import (Any,
                    Iterable,
                    Sequence,
                    Set,
                    Tuple,
                    List)

memoized_primes = {1: False,
                   2: True}

multiply = partial(reduce, operator.mul)

concatenate_iterables = chain.from_iterable


def chunks(elements: Sequence[Any],
           size: int) -> Iterable[Sequence[Any]]:
    elements_count = len(elements)
    for offset in range(elements_count):
        yield elements[offset:offset + size]


def rotate(sequence: Sequence[Any],
           position: int) -> Sequence[Any]:
    return sequence[position:] + sequence[:position]


def parse_lines(lines: Iterable[str],
                *,
                sep: str = ',',
                strip_chars: str = '"') -> Iterable[str]:
    for line in lines:
        yield from (word.strip(strip_chars)
                    for word in line.split(sep))


def max_factor(number: int) -> int:
    return int(sqrt(number))


def max_number(digits_count: int) -> int:
    return 10 ** digits_count - 1


def number_digits_sum(number: int) -> int:
    return sum(number_to_digits(number))


def number_digits_count(number: int) -> int:
    return len(str(number))


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


def fibonacci_numbers(stop: Real = float('inf')) -> Iterable[int]:
    a, b = 0, 1
    while b < stop:
        yield b
        a, b = b, a + b


def prime_numbers(stop: int,
                  *,
                  reverse: bool = False) -> List[int]:
    # based on
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    # TODO: refactor this mess
    if not reverse:
        yield 2
        yield 3

    if stop < 5:
        if reverse:
            yield 3
            yield 2
        return

    stop_mod_six = stop % 6
    correction = stop_mod_six > 1
    stop = {0: stop,
            1: stop - 1,
            2: stop + 4,
            3: stop + 3,
            4: stop + 2,
            5: stop + 1}[stop_mod_six]
    sieve = primes_sieve(stop)

    indices = range(1, stop // 3 - correction)
    if reverse:
        indices = reversed(indices)
    yield from (3 * index + 1 | 1
                for index in indices
                if sieve[index])

    if reverse:
        yield 3
        yield 2


def primes_sieve(stop: int) -> List[bool]:
    sieve = [True] * (stop // 3)
    sieve[0] = False
    factor_stop = max_factor(stop) // 3 + 1
    for factor in range(factor_stop):
        if not sieve[factor]:
            continue

        k = 3 * factor + 1 | 1
        k_squared = k ** 2
        k_doubled = 2 * k
        number_sixth_part_pred = stop // 6 - 1
        sieve[(k_squared // 3)::k_doubled] = (
            [False]
            * ((number_sixth_part_pred - k_squared // 6) // k + 1))

        k_diff = k_squared + 4 * k - k_doubled * (factor & 1)
        sieve[k_diff // 3::k_doubled] = (
            [False]
            * ((number_sixth_part_pred - k_diff // 6) // k + 1))
    return sieve


def odd(number: int) -> int:
    return number & 1


def prime(number: int) -> bool:
    try:
        return memoized_primes[number]
    except KeyError:
        if not odd(number):
            return False
        odd_factors = range(3, max_factor(number) + 1, 2)
        for factor in odd_factors:
            if number % factor == 0:
                result = False
                break
        else:
            result = True
        memoized_primes[number] = result
        return result


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def pythagorean_triplets(stop: int) -> Iterable[int]:
    yield from set(filter(is_pythagorean_triplet,
                          pythagorean_triplets_candidates(stop)))


def is_pythagorean_triplet(triplet: Tuple[int, int, int]) -> bool:
    a, b, c = triplet
    return a ** 2 + b ** 2 == c ** 2


def pythagorean_triplets_candidates(stop: int
                                    ) -> Iterable[Tuple[int, int, int]]:
    # based on
    # https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    min_n = 1
    min_m = 2
    max_k = stop // (min_n ** 2 + min_m ** 2)
    for k in range(1, max_k + 1):
        numbers = range(1, max_factor(stop // k))
        for n, m in map(sorted, permutations(numbers, r=2)):
            candidate = sorted([m ** 2 - n ** 2,
                                2 * m * n,
                                m ** 2 + n ** 2])
            yield tuple(k * coordinate
                        for coordinate in candidate)


def triangular(number: int) -> bool:
    discriminant = 1 + 8 * number
    return is_perfect_square(discriminant)


def pentagonial(number: int) -> bool:
    discriminant = 1 + 24 * number
    return (is_perfect_square(discriminant) and
            (1 + int_sqrt(discriminant)) % 6 == 0)


def is_perfect_square(number: int) -> bool:
    try:
        integer_square_root = int_sqrt(number)
    except ValueError:
        return False
    return integer_square_root * integer_square_root == number


def int_sqrt(number: int) -> int:
    return int(sqrt(number))


def binomial_coefficient(n: int, k: int) -> int:
    numerators = range(n - k + 1, n + 1)
    return multiply(numerators) // factorial(k)
