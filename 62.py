from typing import (Iterable,
                    Set,
                    Tuple)

from utils import (number_to_digits,
                   map_tuples,
                   collect_mapping)


def number_to_sorted_digits_tuple(number: int) -> Tuple[int, ...]:
    return tuple(sorted(number_to_digits(number)))


def cubic_permutations(*,
                       start: int = 1,
                       stop: int,
                       step: int = 1) -> Iterable[Set[int]]:
    numbers = range(start, stop, step)
    cubes = [number ** 3
             for number in numbers]
    digits_cubes = map_tuples(cubes,
                              function=number_to_sorted_digits_tuple)
    yield from collect_mapping(digits_cubes).values()


first_three_elements_permutation = next(
    permutation
    for permutation in cubic_permutations(stop=10_000)
    if len(permutation) == 3)
first_five_elements_permutation = next(
    permutation
    for permutation in cubic_permutations(stop=10_000)
    if len(permutation) == 5)

assert first_three_elements_permutation == [41_063_625, 56_623_104, 66_430_125]
assert first_five_elements_permutation == [127_035_954_683, 352_045_367_981,
                                           373_559_126_408, 569_310_543_872,
                                           589_323_567_104]
assert min(first_five_elements_permutation) == 127_035_954_683
