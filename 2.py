from typing import Iterable


def fibonacci(stop: int) -> Iterable[int]:
    a, b = 0, 1
    while b < stop:
        yield b
        a, b = b, a + b


def is_even(number: int) -> bool:
    return number % 2 == 0


assert sum(filter(is_even, fibonacci(4_000_000))) == 4_613_732
