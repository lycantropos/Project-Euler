def sum_of_digits(number: int) -> int:
    return sum(map(int, str(number)))


assert sum_of_digits(2 ** 15) == 26
assert sum_of_digits(2 ** 1000) == 1_366
