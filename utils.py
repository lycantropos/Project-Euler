import operator
from functools import (partial,
                       reduce)

product = partial(reduce, operator.mul)
