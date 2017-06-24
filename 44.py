from itertools import count

from utils import pentagonal


def pentagonal_number(index: int) -> int:
    return index * (3 * index - 1) // 2


# TODO: improve this "bruteforcefully" working function
def pentagonal_numbers(offset: int) -> int:
    for j in count(1):
        p_j = pentagonal_number(j)
        for s in range(j + 1, j + offset):
            p_s = pentagonal_number(s)
            p_k = p_s - p_j
            p_d = p_k - p_j

            if pentagonal(p_k) and pentagonal(p_d):
                break
        else:
            continue

        return p_k - p_j


assert pentagonal_numbers(offset=10_000) == 5_482_660
