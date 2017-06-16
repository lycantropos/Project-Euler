from typing import (Iterable,
                    Tuple)

from utils import (digits_to_number,
                   is_prime)

possible_digits = {2} | set(range(1, 10, 2))


def truncatable_primes(digits: Tuple[int] = ()) -> Iterable[int]:
    candidate_digits_count = len(digits) + 1
    for digit in possible_digits:
        candidate_digits = (digit,) + digits
        candidate_number = digits_to_number(candidate_digits)
        if not is_prime(candidate_number):
            continue

        if (candidate_digits_count > 1 and
                all(is_prime(digits_to_number(candidate_digits[:position]))
                    for position in range(1, candidate_digits_count))):
            yield candidate_number

        yield from truncatable_primes(candidate_digits)


assert sum(truncatable_primes()) == 748_317
