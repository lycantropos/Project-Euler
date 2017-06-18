from utils import (fibonacci_numbers,
                   number_digits_count)


def n_digits_fibonacci_number_index(digits_count: int) -> int:
    def has_n_digits(number: int) -> bool:
        return number_digits_count(number) >= digits_count

    return next(index
                for index, number in enumerate(fibonacci_numbers(), start=1)
                if has_n_digits(number))


assert n_digits_fibonacci_number_index(1) == 1
assert n_digits_fibonacci_number_index(2) == 7
assert n_digits_fibonacci_number_index(3) == 12
assert n_digits_fibonacci_number_index(1_000) == 4_782
