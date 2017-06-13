from math import factorial

from utils import digits_sum

assert digits_sum(factorial(10)) == 27
assert digits_sum(factorial(100)) == 648
