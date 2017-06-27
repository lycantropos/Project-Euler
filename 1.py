from typing import (Iterable,
                    List)


def multiples(*,
              numbers: Iterable[int],
              multipliers: List[int]
              ) -> Iterable[int]:
    def is_multiple(number: int) -> bool:
        return any(number % multiplier == 0
                   for multiplier in multipliers)

    return filter(is_multiple, numbers)


assert sum(multiples(numbers=range(1, 10),
                     multipliers=[3, 5])) == 23
assert sum(multiples(numbers=range(1, 1_000),
                     multipliers=[3, 5])) == 233_168
