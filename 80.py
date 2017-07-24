from decimal import (Decimal,
                     Context)
from functools import partial
from itertools import filterfalse

from utils import is_perfect_square


def square_root(number: int,
                *,
                digits_count: int) -> Decimal:
    context = Context(prec=digits_count + 2)
    return Decimal(number).sqrt(context)


def digits_sum(number: Decimal,
               *,
               digits_count: int) -> int:
    number_string = str(number)
    digits = number_string.replace('.', '')[:digits_count]
    return sum(map(int, digits))


def square_root_digits_sum(number: int,
                           *,
                           digits_count: int) -> int:
    return digits_sum(square_root(number,
                                  digits_count=digits_count),
                      digits_count=digits_count)


first_hundred_square_root_digits_sum = partial(square_root_digits_sum,
                                               digits_count=100)
non_perfect_square_numbers = filterfalse(is_perfect_square, range(1, 101))

assert first_hundred_square_root_digits_sum(2) == 475
assert (sum(map(first_hundred_square_root_digits_sum,
                non_perfect_square_numbers))) == 40_886
