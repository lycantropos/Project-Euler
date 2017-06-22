# if we take a look at consecutive spirals
# dimension = 1
# |01|
# dimension = 3
# |07|08|09|
# |06|01|02|
# |05|04|03|
# dimension = 5
# |21|22|23|24|25|
# |20|07|08|09|10|
# |19|06|01|02|11|
# |18|05|04|03|12|
# |17|16|15|14|13|
# we can see that in top right corner there's always squared dimension
# and values on other corners can be found by subtraction of (dimension - 1)
# from previous corner in counterclockwise direction
from itertools import chain

from utils import (SPIRAL_START,
                   spiral_corners)


def number_spiral_diagonals(dimension: int,
                            *,
                            start=SPIRAL_START) -> int:
    return sum((chain
                .from_iterable(spiral_corners(dimension,
                                              start=start))),
               start)


assert number_spiral_diagonals(1) == 1
assert number_spiral_diagonals(5) == 101
assert number_spiral_diagonals(1_001) == 669_171_001
