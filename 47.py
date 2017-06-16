from itertools import count
from typing import List

from utils import (prime,
                   factors)


def distinct_primes_factors(*,
                            consecutive_numbers_count: int = 4,
                            distinct_prime_factors_count: int = 4
                            ) -> List[int]:
    numbers_count = 0
    consecutive_numbers = []
    for number in count(1):
        if numbers_count == consecutive_numbers_count:
            break

        prime_factors = set(filter(prime, factors(number)))

        if len(prime_factors) != distinct_prime_factors_count:
            numbers_count = 0
            consecutive_numbers[:] = []
            continue

        consecutive_numbers.append(number)
        numbers_count += 1

    return consecutive_numbers


assert distinct_primes_factors(consecutive_numbers_count=2,
                               distinct_prime_factors_count=2) == [14, 15]
assert distinct_primes_factors(consecutive_numbers_count=3,
                               distinct_prime_factors_count=3) == [644, 645, 646]
assert min(distinct_primes_factors(consecutive_numbers_count=4,
                                   distinct_prime_factors_count=4)) == 134_043
