from itertools import permutations
from typing import (Iterable,
                    Dict)

from utils import (primes,
                   digits_to_number,
                   number_to_digits)


def sub_string_divisible_numbers(*,
                                 digits: Iterable[int],
                                 slicers_by_divisors: Dict[int, slice]
                                 ) -> Iterable[int]:
    for digits in permutations(digits):
        number = digits_to_number(digits)
        digits = list(number_to_digits(number))
        for divisor, slicer in slicers_by_divisors.items():
            digits_slice = digits[slicer]
            sliced_number = digits_to_number(digits_slice)
            if sliced_number % divisor:
                break
        else:
            yield number


primes_generator = primes(18)
slicers_by_divisors = {next(primes_generator): slice(start - 1, start + 2)
                       for start in range(2, 9)}

assert sum(sub_string_divisible_numbers(
    digits=range(10),
    slicers_by_divisors=slicers_by_divisors)) == 16_695_334_890
