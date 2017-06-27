from typing import Iterable


def self_powers(numbers: Iterable[int]) -> Iterable[int]:
    for number in numbers:
        yield number ** number


assert sum(self_powers(range(1, 11))) == 10_405_071_317
assert str(sum(self_powers(range(1, 1_001))))[-10:] == '9110846700'
