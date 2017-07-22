from functools import partial

from utils import (map_tuples,
                   collect_mapping,
                   has_n_elements,
                   integer_right_triangles)

pythagorean_triplets_by_perimeters = collect_mapping(
    map_tuples(integer_right_triangles(1_500_000),
               function=sum))
has_one_element = partial(has_n_elements,
                          n=1)
assert sum(map(has_one_element,
               pythagorean_triplets_by_perimeters.values())) == 161_667
