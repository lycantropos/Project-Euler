from itertools import count

from utils import (factors,
                   prime)

memoized_sum_of_prime_factors = dict()


def sum_of_prime_factors(number: int) -> int:
    try:
        return memoized_sum_of_prime_factors[number]
    except KeyError:
        result = sum(filter(prime, factors(number)))
        memoized_sum_of_prime_factors[number] = result
        return result


memoized_prime_partitions = {0: 0}


def prime_partitions(number: int) -> int:
    try:
        return memoized_prime_partitions[number]
    except KeyError:
        # based on
        # https://programmingpraxis.com/2012/10/19/prime-partitions/#comment-5762
        increment = sum(sum_of_prime_factors(offset)
                        * prime_partitions(number - offset)
                        for offset in range(1, number))
        result = (sum_of_prime_factors(number) + increment) // number
        memoized_prime_partitions[number] = result
        return result


assert prime_partitions(10) == 5
assert next(number
            for number in count(1)
            if prime_partitions(number) >= 5_000) == 71
