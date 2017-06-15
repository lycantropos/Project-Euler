from utils import (primes,
                   number_digits_count,
                   max_number,
                   digits_to_number,
                   number_to_digits,
                   rotate)


def circular_primes(number: int):
    primes_stop = max_number(number_digits_count(number))
    primes_set = set(primes(primes_stop))

    def is_circular(prime) -> bool:
        digits = tuple(number_to_digits(prime))
        rotated_digits = (rotate(digits, position)
                          for position in range(len(digits)))
        for rotated_prime in map(digits_to_number, rotated_digits):
            if rotated_prime not in primes_set:
                return False
        return True

    yield from filter(is_circular, primes(number))


assert list(circular_primes(100)) == [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
assert sum(1 for _ in circular_primes(1_000_000)) == 55
