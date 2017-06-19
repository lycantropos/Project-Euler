# Lattice paths counts for 2x2 grid:
# 6__3__1
# |  |  |
# 3__2__1
# |  |  |
# 1__1__1
# Let's rotate this grid by 3 * pi / 4
#     1
#    / \
#   1   1
#  / \ / \
# 1   2   1
#  \ / \ /
#   3   3
#    \ /
#     6
# We can see that this is a part of Pascal triangle,
# and paths count from top left corner to bottom right corner
# for 2x2 grid can be found as "4 choose 2",
# where 4 is the level of Pascal triangle
# and 2 is the position of bottom right corner after rotation.
# Finally for NxN grid paths count can be found as "2 * N choose N".

from utils import binomial_coefficient


def lattice_paths(grid_order: int) -> int:
    return binomial_coefficient(2 * grid_order, grid_order)


assert lattice_paths(2) == 6
assert lattice_paths(20) == 137_846_528_820
