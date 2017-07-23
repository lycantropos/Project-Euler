from utils import factors

memoized_sum_of_factors = {}


def sum_of_factors(number: int) -> int:
    try:
        return memoized_sum_of_factors[number]
    except KeyError:
        result = sum(factors(number))
        memoized_sum_of_factors[number] = result
        return result


memoized_partitions = {0: 1}


def partitions(number: int) -> int:
    try:
        return memoized_partitions[number]
    except KeyError:
        # based on
        # https://en.wikipedia.org/wiki/Partition_(number_theory)#Other_recurrence_relations
        result = sum(sum_of_factors(number - offset)
                     * partitions(offset)
                     for offset in range(number)) // number
        memoized_partitions[number] = result
        return result


assert partitions(5) - 1 == 6
assert partitions(100) - 1 == 190_569_291
