from itertools import count

from utils import pentagonial


def pentagonial_number(index: int) -> int:
    return index * (3 * index - 1) // 2


# TODO: improve this "bruteforcefully" working function
def pentagon_numbers(offset: int) -> int:
    for j in count(1):
        p_j = pentagonial_number(j)
        for s in range(j + 1, j + offset):
            p_s = pentagonial_number(s)
            p_k = p_s - p_j
            p_d = p_k - p_j

            if pentagonial(p_k) and pentagonial(p_d):
                break
        else:
            continue

        return p_k - p_j


assert pentagon_numbers(offset=10_000) == 5_482_660
