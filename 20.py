from math import factorial

from utils import sum_of_digits

assert sum_of_digits(factorial(10)) == 27
assert sum_of_digits(factorial(100)) == 648
