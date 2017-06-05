def sqr(number: int) -> int:
    return number ** 2


def sum_of_squares(*,
                   start: int = 1,
                   stop: int,
                   step: int = 1) -> int:
    numbers = range(start, stop, step)
    return sum(map(sqr, numbers))


def square_of_sum(*,
                  start: int = 1,
                  stop: int,
                  step: int = 1) -> int:
    numbers = range(start, stop, step)
    return sqr(sum(numbers))


def sum_square_difference(*,
                          start: int = 1,
                          stop: int,
                          step: int = 1) -> int:
    minuend = square_of_sum(start=start, stop=stop, step=step)
    subtrahend = sum_of_squares(start=start, stop=stop, step=step)
    return minuend - subtrahend


assert sum_square_difference(stop=11) == 2_640
assert sum_square_difference(stop=101) == 25_164_150
