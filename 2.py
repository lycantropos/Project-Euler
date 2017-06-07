from itertools import filterfalse
from typing import Iterable

from utils import odd


def fibonacci(stop: int) -> Iterable[int]:
    a, b = 0, 1
    while b < stop:
        yield b
        a, b = b, a + b


assert sum(filterfalse(odd, fibonacci(4_000_000))) == 4_613_732
