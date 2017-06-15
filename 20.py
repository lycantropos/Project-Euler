from math import factorial

from utils import number_digits_sum

assert number_digits_sum(factorial(10)) == 27
assert number_digits_sum(factorial(100)) == 648
