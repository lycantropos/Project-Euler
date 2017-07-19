from utils import n_phi

example_totient_maximum_argument = max(range(2, 11),
                                       key=n_phi)
totient_maximum_argument = max(range(2, 1_000_001),
                               key=n_phi)

assert example_totient_maximum_argument == 6
assert totient_maximum_argument == 510_510
