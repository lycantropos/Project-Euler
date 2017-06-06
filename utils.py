import operator
from functools import (partial,
                       reduce)
from typing import (Any,
                    Iterable,
                    Sequence)

multiply = partial(reduce, operator.mul)


def chunks(elements: Sequence[Any],
           size: int) -> Iterable[Sequence[Any]]:
    elements_count = len(elements)
    for offset in range(elements_count):
        yield elements[offset:offset + size]
