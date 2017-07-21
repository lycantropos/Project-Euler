from utils import n_phi

example_totient_maximum_argument = max(range(10, 1, -1),
                                       key=n_phi)
totient_maximum_argument = max(range(1_000_000, 1, -1),
                               key=n_phi)

assert example_totient_maximum_argument == 6
assert totient_maximum_argument == 510_510
