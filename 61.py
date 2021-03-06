from functools import partial
from itertools import permutations
from typing import (Any,
                    Iterable,
                    Sequence,
                    Dict,
                    Tuple,
                    List)

from utils import (collect_mapping,
                   polygonal,
                   sort_permutation,
                   bisect)


def posterity(parent: str,
              relations_group: Iterable[Dict[str, Sequence[str]]]
              ) -> Iterable[List[str]]:
    try:
        relations, *rest = relations_group
        children = relations[parent]
    except (ValueError, KeyError):
        yield [parent]
    else:
        for child in children:
            for descendants in posterity(child, rest):
                yield [parent] + descendants


def paths(relations_group: Iterable[Dict[str, Sequence[str]]]
          ) -> List[str]:
    relations, *rest = relations_group

    for parent, children in relations.items():
        for child in children:
            for descendants in posterity(child,
                                         relations_group=rest):
                yield [parent] + descendants


def cycled(path: Sequence[Any]) -> bool:
    return path[0] == path[-1]


def cyclical_polygonal_numbers(*,
                               numbers: Iterable[int],
                               dimensions: Sequence[int]
                               ) -> Tuple[int, ...]:
    polygonals_filters = {dimension: partial(polygonal,
                                             dimension=dimension)
                          for dimension in dimensions}
    polygonals_numbers = {
        dimension: list(filter(polygonal_filter, numbers))
        for dimension, polygonal_filter in polygonals_filters.items()}
    polygonal_numbers_strings = (list(map(str, numbers))
                                 for numbers in polygonals_numbers.values())
    polygonals_numbers_parts = dict(
        zip(polygonals_numbers.keys(),
            map(collect_mapping,
                (map(bisect, numbers_strings)
                 for numbers_strings in polygonal_numbers_strings))))

    keys_permutations = set(map(sort_permutation,
                                permutations(polygonals_numbers_parts)))
    for keys_permutation in keys_permutations:
        mappings = [polygonals_numbers_parts[key]
                    for key in keys_permutation]
        cycled_paths = filter(cycled, map(tuple, paths(mappings)))
        for path in cycled_paths:
            yield tuple(int(digits + next_digits)
                        for digits, next_digits in zip(path, path[1:]))


triangular_to_pentagonal_cycle = max(
    cyclical_polygonal_numbers(numbers=range(1_000, 10_000),
                               dimensions=range(3, 6)),
    key=len)
triangular_to_octagonal_cycle = max(
    cyclical_polygonal_numbers(numbers=range(1_000, 10_000),
                               dimensions=range(3, 9)),
    key=len)

assert triangular_to_pentagonal_cycle == (8_128, 2_882, 8_281)
assert triangular_to_octagonal_cycle == (8_256, 5_625, 2_512,
                                         1_281, 8_128, 2_882)
assert sum(triangular_to_octagonal_cycle) == 28_684
