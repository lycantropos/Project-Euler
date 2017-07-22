import operator
from functools import partial
from itertools import (chain,
                       permutations)
from typing import (Iterable,
                    Tuple,
                    List)

from utils import has_n_elements

LINE_LENGTH = 3
MagicNGonRingType = List[Tuple[int, int, int]]


def ring_to_string(ring: MagicNGonRingType) -> str:
    return ''.join(map(str, chain(*ring)))


def magic_n_gon_rings(numbers: Iterable[int],
                      *,
                      n: int) -> Iterable[MagicNGonRingType]:
    for line in permutations(numbers, LINE_LENGTH):
        first_start = line[0]
        target_sum = sum(line)
        rest_numbers = set(numbers) - set(line)
        next_starts_candidates = filter(partial(operator.lt,
                                                first_start),
                                        rest_numbers)
        for next_starts in permutations(next_starts_candidates,
                                        r=n - 1):
            ring = [line]
            next_ends_candidates = rest_numbers - set(next_starts)
            next_middle = line[-1]
            *next_starts, last_start = next_starts
            for next_start in next_starts:
                next_end = target_sum - next_start - next_middle
                if next_end not in next_ends_candidates:
                    break
                next_line = next_start, next_middle, next_end
                ring.append(next_line)
                next_middle = next_end
            else:
                last_line = last_start, next_middle, line[1]
                if sum(last_line) != target_sum:
                    continue
                ring.append(last_line)
                yield ring


# reversing numbers order gives us maximum on the first entry
magic_3_gon_rings = magic_n_gon_rings(range(6, 0, -1),
                                      n=3)
magic_3_gon_rings_strings = map(ring_to_string,
                                magic_3_gon_rings)
magic_5_gon_rings = magic_n_gon_rings(range(10, 0, -1),
                                      n=5)
magic_5_gon_rings_strings = map(ring_to_string,
                                magic_5_gon_rings)

assert next(magic_3_gon_rings_strings) == '432621513'
assert next(filter(partial(has_n_elements,
                           n=16),
                   magic_5_gon_rings_strings)) == '6531031914842725'
