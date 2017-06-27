from typing import Iterable

from utils import odd

memoized_collatz_sequences_lengths = {}


def collatz_sequence_length(start: int) -> Iterable[int]:
    term = start
    length = 1
    while term != 1:
        if not odd(term):
            term //= 2
        else:
            term = 3 * term + 1
        try:
            length += memoized_collatz_sequences_lengths[term]
            break
        except KeyError:
            length += 1
    memoized_collatz_sequences_lengths[start] = length
    return length


assert collatz_sequence_length(13) == 10
assert max(range(1, 1_000_000),
           key=collatz_sequence_length) == 837_799
