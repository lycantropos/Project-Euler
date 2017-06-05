from typing import Generator


def fibonacci(stop: int) -> Generator[int, None, None]:
    a, b = 0, 1
    while b < stop:
        yield b
        a, b = b, a + b


def is_even(number: int) -> bool:
    return number % 2 == 0


print(sum(filter(is_even, fibonacci(4_000_000))))
