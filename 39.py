from collections import Counter
from typing import (Iterable,
                    Tuple)

from utils import pythagorean_triplets


def integer_right_triangles(max_perimeter: int
                            ) -> Iterable[Tuple[int, int, int]]:
    def is_perimeter_valid(triplet: Tuple[int, int, int]) -> bool:
        return sum(triplet) <= max_perimeter

    yield from filter(is_perimeter_valid,
                      pythagorean_triplets(max_perimeter))


perimeters_counter = Counter(map(sum, integer_right_triangles(1_000)))
(most_common_perimeter, _), = perimeters_counter.most_common(1)

assert most_common_perimeter == 840
