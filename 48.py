from typing import Iterable


def self_powers(*,
                start: int = 1,
                stop: int,
                step: int = 1) -> Iterable[int]:
    for number in range(start, stop, step):
        yield number ** number


assert sum(self_powers(stop=11)) == 10_405_071_317
assert str(sum(self_powers(stop=1_001)))[-10:] == '9110846700'
