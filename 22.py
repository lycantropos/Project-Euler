from string import ascii_uppercase
from typing import Iterable

from utils import parse_lines


def alphabetical_value(word: str) -> int:
    return sum(index + 1
               for index in map(ascii_uppercase.index, word))


def total_names_score(names: Iterable[str]) -> int:
    sorted_names = sorted(names)
    return sum(index * alphabetical_value(name)
               for index, name in enumerate(sorted_names, start=1))


with open('names.txt') as names_file:
    names = list(parse_lines(names_file))

assert alphabetical_value('COLIN') == 53
assert total_names_score(names) == 871_198_282
