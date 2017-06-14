from itertools import permutations
from math import ceil
from typing import Iterable


def pandigital_products(digits: Iterable[int]):
    digits = set(digits)
    digits_count = len(digits)
    multipliers_digits_counts_sum = ceil(digits_count / 2)
    product_multiplier_digits_count = digits_count - multipliers_digits_counts_sum
    max_left_multipliers_digits_count = ceil((multipliers_digits_counts_sum - 1) / 2)
    for left_multiplier_digits_count in range(1, max_left_multipliers_digits_count + 1):
        right_multiplier_digits_count = (multipliers_digits_counts_sum
                                         - left_multiplier_digits_count)
        left_multipliers_digits = permutations(digits,
                                               r=left_multiplier_digits_count)
        for left_multiplier_digits in left_multipliers_digits:
            allowed_right_multipliers_digits = digits - set(left_multiplier_digits)
            right_multipliers_digits = permutations(allowed_right_multipliers_digits,
                                                    r=right_multiplier_digits_count)
            for right_multiplier_digits in right_multipliers_digits:
                allowed_products_digits = (allowed_right_multipliers_digits
                                           - set(right_multiplier_digits))
                products_digits = permutations(allowed_products_digits,
                                               r=product_multiplier_digits_count)
                for product_digits in products_digits:
                    left_multiplier = digits_to_number(left_multiplier_digits)
                    right_multiplier = digits_to_number(right_multiplier_digits)
                    product = digits_to_number(product_digits)
                    if left_multiplier * right_multiplier == product:
                        yield product


def digits_to_number(digits: Iterable[int]) -> int:
    return int(''.join(map(str, digits)))


assert sum(set(pandigital_products(range(1, 10)))) == 45_228
