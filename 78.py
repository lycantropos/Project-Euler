from itertools import count

from utils import partitions

assert partitions(5) == 7
assert next(number
            for number in count(1)
            if partitions(number) % 1_000_000 == 0) == 55_374
