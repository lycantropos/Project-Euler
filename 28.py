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


def number_spiral_diagonals(dimension: int) -> int:
    result = 1
    for turn in range(3, dimension + 2, 2):
        decrement = turn - 1
        right_top_number = turn * turn
        left_top_number = right_top_number - decrement
        left_bottom_number = left_top_number - decrement
        right_bottom_number = left_bottom_number - decrement
        result += (right_top_number
                   + left_top_number
                   + left_bottom_number
                   + right_bottom_number)
    return result


assert number_spiral_diagonals(1) == 1
assert number_spiral_diagonals(5) == 101
assert number_spiral_diagonals(1_001) == 669_171_001
