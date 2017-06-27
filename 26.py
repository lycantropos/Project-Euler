from decimal import (Decimal,
                     getcontext)
from itertools import filterfalse

getcontext().prec = 1_000

EMPTY_CYCLE = ''


def recurring_cycle(number: Decimal) -> str:
    try:
        number_str = str(number)
        _, fractional_part = number_str.split('.')
        # trailing zeros are not representative
        fractional_part = fractional_part.rstrip('0')
    except ValueError:
        # no fractional part
        return EMPTY_CYCLE

    while fractional_part:
        length = 1
        digits_count = len(fractional_part)
        while length < digits_count:
            cycle = fractional_part[:length]

            def is_cycle(occurrence) -> bool:
                return occurrence == cycle

            occurrences = (fractional_part[offset: offset + length]
                           for offset in range(length, digits_count, length))
            non_cycle_occurrences = filterfalse(is_cycle, occurrences)
            try:
                tail = next(non_cycle_occurrences)
            except StopIteration:
                # all occurrences are equal to cycle
                return cycle

            try:
                next(non_cycle_occurrences)
            except StopIteration:
                cycle_start = cycle[:len(tail)]
                next_digit_after_tail = cycle[len(tail):len(tail) + 1]
                next_digit_after_tail = (int(next_digit_after_tail)
                                         if next_digit_after_tail
                                         else 0)
                tail_diff = int(tail) - int(cycle_start)
                tail_is_periodic = (next_digit_after_tail < 5 and
                                    tail_diff == 0 or
                                    next_digit_after_tail >= 5 and
                                    tail_diff == 1)
                if tail_is_periodic:
                    return cycle

            length += 1
            continue

        fractional_part = fractional_part[1:]
    return EMPTY_CYCLE


def unit_fraction(denominator: int) -> Decimal:
    return Decimal(1) / Decimal(denominator)


def unit_fraction_recurring_cycle_length(denominator: int) -> int:
    return len(recurring_cycle(unit_fraction(denominator)))


def longest_recurring_cycle(denominators) -> int:
    return max(denominators,
               key=unit_fraction_recurring_cycle_length)


assert longest_recurring_cycle(range(85, 1_000, 2)) == 983
