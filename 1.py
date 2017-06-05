from typing import (Iterable,
                    List)


def multiples(*,
              start: int = 1,
              stop: int,
              step: int = 1,
              multipliers: List[int]
              ) -> Iterable[int]:
    numbers = range(start, stop, step)

    def is_multiple(number: int) -> bool:
        return any(number % multiplier == 0
                   for multiplier in multipliers)

    return filter(is_multiple, numbers)


assert sum(multiples(stop=1_000,
                     multipliers=[3, 5])) == 233_168
