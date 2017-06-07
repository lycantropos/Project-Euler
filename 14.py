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


def longest_collatz_sequence(*,
                             start: int = 1,
                             stop: int,
                             step: int = 1) -> int:
    return max(range(start, stop, step),
               key=collatz_sequence_length)


assert collatz_sequence_length(13) == 10
assert longest_collatz_sequence(stop=1_000_000) == 837_799
