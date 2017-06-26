from decimal import (Decimal,
                     Context,
                     setcontext)
from itertools import (count,
                       islice,
                       filterfalse)
from typing import (Any,
                    Optional,
                    Iterable,
                    Sequence)

from utils import (is_perfect_square,
                   odd)


def find_cycle(sequence: Sequence[Any]) -> Optional[Sequence[Any]]:
    elements_count = len(sequence)
    for cycle_stop in range(1, elements_count):
        cycle = sequence[:cycle_stop]
        candidates = (sequence[offset: offset + cycle_stop]
                      for offset in reversed(range(cycle_stop,
                                                   elements_count,
                                                   cycle_stop)))
        last_candidate = next(candidates)
        if (cycle[:len(last_candidate)] == last_candidate and
                all(candidate == cycle
                    for candidate in candidates)):
            return cycle


def continued_fraction(number: int) -> Iterable[int]:
    memoized_b_coefficients = {0: Decimal(number).sqrt()}

    def b_coefficient(index: int) -> Decimal:
        try:
            return memoized_b_coefficients[index]
        except KeyError:
            b_prev = b_coefficient(index - 1)
            a_prev = int(b_prev)
            numerator = b_prev + a_prev
            denominator = numerator * (b_prev - a_prev)
            coefficient = numerator / denominator
            memoized_b_coefficients[index] = coefficient
            return coefficient

    for index in count():
        yield int(b_coefficient(index))


def odd_period_square_roots(*,
                            start: int = 1,
                            stop: int,
                            step: int = 1,
                            members_count_start: int = 250,
                            members_count_step: int = 50,
                            precision_start: int = 500,
                            precision_step: int = 250,
                            precision_stop: int = 2_501) -> int:
    numbers = range(start, stop, step)
    numbers = list(filterfalse(is_perfect_square, numbers))
    cycles_lengths = map(len,
                         periods(numbers,
                                 members_count_start=members_count_start,
                                 members_count_step=members_count_step,
                                 precision_start=precision_start,
                                 precision_step=precision_step,
                                 precision_stop=precision_stop))
    return sum(map(odd, cycles_lengths))


def periods(numbers: Iterable[int],
            *,
            members_count_start: int,
            members_count_step: int,
            precision_start: int,
            precision_step: int,
            precision_stop: int) -> Sequence[int]:
    for number in numbers:
        for members_count in count(members_count_start,
                                   members_count_step):
            for precision in range(precision_start,
                                   precision_stop,
                                   precision_step):
                context = Context(prec=precision)
                setcontext(context)
                sequence = list(islice(continued_fraction(number),
                                       1,
                                       members_count))
                cycle = find_cycle(sequence)
                if cycle is None:
                    continue
                yield cycle
                break
            else:
                continue
            break


assert odd_period_square_roots(stop=14) == 4
assert odd_period_square_roots(stop=10_001) == 1_322
