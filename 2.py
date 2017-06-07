from itertools import filterfalse

from utils import odd, fibonacci

assert sum(filterfalse(odd, fibonacci(4_000_000))) == 4_613_732
