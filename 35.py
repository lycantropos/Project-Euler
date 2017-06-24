from typing import Iterable

from utils import (prime_numbers,
                   number_digits_count,
                   max_number,
                   digits_to_number,
                   number_to_digits,
                   rotate,
                   capacity)


def circular_primes(stop: int) -> Iterable[int]:
    primes_stop = max_number(number_digits_count(stop))
    primes_set = set(prime_numbers(primes_stop))

    def circular(prime_number: int) -> bool:
        digits = tuple(number_to_digits(prime_number))
        rotated_digits = (rotate(digits, position)
                          for position in range(len(digits)))
        for rotated_prime in map(digits_to_number, rotated_digits):
            if rotated_prime not in primes_set:
                return False
        return True

    yield from filter(circular, prime_numbers(stop))


assert list(circular_primes(100)) == [2, 3, 5, 7, 11, 13, 17,
                                      31, 37, 71, 73, 79, 97]
assert capacity(circular_primes(1_000_000)) == 55
