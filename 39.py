from collections import Counter

from utils import integer_right_triangles

perimeters_counter = Counter(map(sum, integer_right_triangles(1_000)))
(most_common_perimeter, _), = perimeters_counter.most_common(1)

assert most_common_perimeter == 840
