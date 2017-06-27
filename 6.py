from typing import (Iterable,
                    Sequence)


def sqr(number: int) -> int:
    return number ** 2


def sum_of_squares(numbers: Iterable[int]) -> int:
    return sum(map(sqr, numbers))


def square_of_sum(numbers: Iterable[int]) -> int:
    return sqr(sum(numbers))


def sum_square_difference(numbers: Sequence[int]) -> int:
    minuend = square_of_sum(numbers)
    subtrahend = sum_of_squares(numbers)
    return minuend - subtrahend


assert sum_square_difference(range(1, 11)) == 2_640
assert sum_square_difference(range(1, 101)) == 25_164_150
