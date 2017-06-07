from itertools import (permutations,
                       islice)
from typing import Iterable


def digits_lexicographic_permutation(*,
                                     digits: Iterable[int],
                                     index: int) -> int:
    return next(islice(permutations(digits), index - 1, index))


assert list(permutations(range(3))) == [(0, 1, 2), (0, 2, 1), (1, 0, 2),
                                        (1, 2, 0), (2, 0, 1), (2, 1, 0)]
assert digits_lexicographic_permutation(digits=range(10),
                                        index=1_000_000) == (2, 7, 8, 3, 9,
                                                             1, 5, 4, 6, 0)
