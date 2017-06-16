from itertools import (count,
                       filterfalse)

from utils import (prime_numbers,
                   prime,
                   is_perfect_square)


def is_prime_and_twice_square_numbers_sum(odd_number: int) -> bool:
    for prime_number in prime_numbers(odd_number):
        square = (odd_number - prime_number) // 2
        if is_perfect_square(square):
            return True
    return False


def goldbach_other_conjecture():
    odd_numbers = count(start=1,
                        step=2)
    # we are skipping 1
    # since it is not prime or composite odd number
    next(odd_numbers)
    odd_composite_numbers = filterfalse(prime,
                                        odd_numbers)
    yield from filterfalse(is_prime_and_twice_square_numbers_sum,
                           odd_composite_numbers)


assert next(goldbach_other_conjecture()) == 5_777
