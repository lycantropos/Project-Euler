from typing import (Iterable,
                    List)


def multiples(*,
              stop_number: int,
              start_number: int = 1,
              step: int = 1,
              multipliers: List[int]
              ) -> Iterable[int]:
    numbers = range(start_number, stop_number, step)

    def is_multiple(number: int) -> bool:
        return any(number % multiplier == 0
                   for multiplier in multipliers)

    return filter(is_multiple, numbers)


print(sum(multiples(stop_number=1000,
                    multipliers=[3, 5])))
