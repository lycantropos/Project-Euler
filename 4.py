from itertools import combinations
from typing import Iterable

from utils import is_palindrome


def numbers_products_palindromes(numbers: Iterable[int]) -> Iterable[int]:
    numbers_products = (number * other_number
                        for number, other_number in combinations(numbers,
                                                                 r=2))
    yield from map(int, filter(is_palindrome, map(str, numbers_products)))


assert max(numbers_products_palindromes(range(10, 100))) == 9_009
assert max(numbers_products_palindromes(range(100, 1_000))) == 906_609
