from utils import factors


def sum_of_divisors(number: int) -> int:
    return sum(factors(number))


memoized_partitions = {0: 1}


def partitions(number: int) -> int:
    try:
        return memoized_partitions[number]
    except KeyError:
        # based on
        # https://en.wikipedia.org/wiki/Partition_(number_theory)#Other_recurrence_relations
        result = sum(sum_of_divisors(number - offset) * partitions(offset)
                     for offset in range(number)) // number
        memoized_partitions[number] = result
        return result


assert partitions(5) - 1 == 6
assert partitions(100) - 1 == 190_569_291
