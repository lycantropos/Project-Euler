from utils import phi


def reduced_proper_fractions_count(max_denominator: int) -> int:
    return sum(map(phi, range(max_denominator, 1, -1)))


assert reduced_proper_fractions_count(8) == 21
assert reduced_proper_fractions_count(1_000_000) == 303_963_552_391
