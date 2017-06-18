from itertools import filterfalse

from utils import (odd,
                   fibonacci_numbers)

assert sum(filterfalse(odd, fibonacci_numbers(4_000_000))) == 4_613_732
