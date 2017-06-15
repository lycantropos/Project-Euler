from itertools import combinations
from typing import Iterable

from utils import is_palindrome


def numbers_products_palindromes(*,
                                 start: int,
                                 stop: int,
                                 step: int = 1) -> Iterable[int]:
    numbers = range(start, stop, step)
    numbers_products = (number * other_number
                        for number, other_number in combinations(numbers,
                                                                 r=2))
    yield from map(int, filter(is_palindrome, map(str, numbers_products)))


assert max(numbers_products_palindromes(start=10,
                                        stop=100)) == 9009
assert max(numbers_products_palindromes(start=100,
                                        stop=1000)) == 906_609
