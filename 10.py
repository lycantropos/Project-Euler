from utils import prime_numbers


def sum_of_primes(stop: int) -> int:
    return sum(prime_numbers(stop))


assert sum_of_primes(10) == 17
assert sum_of_primes(2_000_000) == 142_913_828_922
