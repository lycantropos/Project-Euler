from itertools import combinations
from typing import (Union,
                    Iterable,
                    Tuple)

from utils import (prime_numbers,
                   number_to_digits)


def prime_digit_replacements(stop: int) -> Iterable[int]:
    numbers = list(prime_numbers(stop))
    numbers_digits = map(tuple, map(number_to_digits, numbers))

    digits_wildcards = dict()
    for number, digits in zip(numbers, numbers_digits):
        for wildcard in generate_wildcards(digits):
            digits_wildcards.setdefault(wildcard, []).append(number)
    return digits_wildcards.values()


def generate_wildcards(digits: Tuple[int],
                       wildcard: str = '*'
                       ) -> Iterable[Tuple[Union[str, int], ...]]:
    unique_digits = set(digits)
    for target_digit in unique_digits:
        occurrences = [position
                       for position, digit in enumerate(digits)
                       if digit == target_digit]
        for occurrences_count in range(1, len(occurrences) + 1):
            for occurrences_combination in combinations(occurrences,
                                                        occurrences_count):
                yield tuple(wildcard
                            if position in occurrences_combination
                            else digit
                            for position, digit in enumerate(digits))


assert max(prime_digit_replacements(100),
           key=len) == [13, 23, 43, 53, 73, 83]
assert max(prime_digit_replacements(100_000),
           key=len) == [56003, 56113, 56333, 56443, 56663, 56773, 56993]
assert min(max(prime_digit_replacements(1_000_000),
               key=len)) == 121_313
