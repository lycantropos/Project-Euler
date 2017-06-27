from typing import Iterable

from utils import is_palindrome


def double_base_palindromes(numbers: Iterable[int]) -> Iterable[int]:
    yield from filter(is_double_based_palindrome, numbers)


def is_double_based_palindrome(number: int) -> bool:
    return is_palindrome(str(number)) and is_palindrome(to_binary(number))


def to_binary(number: int) -> str:
    return f'{number:b}'


assert is_double_based_palindrome(585)
assert sum(double_base_palindromes(range(0, 1_000_000))) == 872_187
