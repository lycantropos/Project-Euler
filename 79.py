from itertools import chain
from typing import Iterable

from utils import collect_mapping


def passcode_derivation(logs: Iterable[str]) -> Iterable[str]:
    binary_relations = set(chain.from_iterable((log[:2], log[1:])
                                               for log in logs))
    descendants = []
    hierarchy = collect_mapping(binary_relations)
    while hierarchy:
        all_descendants = sum(hierarchy.values(), [])
        ancestor, = (parent
                     for parent in hierarchy
                     if parent not in all_descendants)
        descendants = hierarchy.pop(ancestor)
        yield ancestor
    yield from descendants


with open('keylog.txt') as keylog_file:
    keylog = set(map(str.rstrip, keylog_file))
assert ''.join(passcode_derivation(keylog)) == '73162890'
