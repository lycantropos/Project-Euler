from typing import Iterable

from utils import even

memoized_collatz_sequences_lengths = {}


def collatz_sequence_length(start: int) -> Iterable[int]:
    term = start
    length = 1
    while term != 1:
        if even(term):
            term //= 2
        else:
            term = 3 * term + 1
        if term in memoized_collatz_sequences_lengths:
            length += memoized_collatz_sequences_lengths[term]
            break
        length += 1
    memoized_collatz_sequences_lengths[start] = length
    return length


def longest_collatz_sequence(stop: int) -> int:
    return max(range(1, stop),
               key=collatz_sequence_length)


assert longest_collatz_sequence(1_000_000) == 837_799
