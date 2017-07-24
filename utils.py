import operator
import re
from decimal import (Decimal,
                     Context,
                     setcontext)
from fractions import Fraction
from functools import (partial,
                       reduce)
from itertools import (chain,
                       permutations,
                       repeat,
                       count,
                       islice)
from math import (sqrt,
                  factorial,
                  gcd)
from numbers import Real
from typing import (Any,
                    Optional,
                    Callable,
                    Hashable,
                    Iterable,
                    Iterator,
                    Collection,
                    Sequence,
                    MutableMapping,
                    MutableSequence,
                    Set,
                    Tuple,
                    List)

SPIRAL_START = 1
WORDS_RE = re.compile(r'\b\w+\b')
FIRST_LETTERS_FOLLOWERS = {
    'a': {'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
          'r', 's', 't', 'u', 'v', 'w', 'x', 'z'},
    'b': {'a', 'e', 'i', 'l', 'o', 'r', 'u', 'y'},
    'c': {'a', 'e', 'h', 'i', 'l',
          'o', 'r', 'u', 'y'},
    'd': {'a', 'e', 'i', 'o', 'r', 'u', 'w', 'y'},
    'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i',
          'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'x', 'y'},
    'f': {'a', 'e', 'i', 'j', 'l', 'o', 'r', 'u'},
    'g': {'a', 'e', 'h', 'i', 'l',
          'n', 'o', 'r', 'u', 'y'},
    'h': {'a', 'e', 'i', 'o', 'u', 'y'},
    'i': {'a', 'b', 'c', 'd', 'f', 'g', 'l',
          'm', 'n', 'o', 'r', 's', 't', 'v'},
    'j': {'a', 'e', 'i', 'o', 'u'},
    'k': {'a', 'e', 'i', 'l', 'n', 'o', 'r', 'u'},
    'l': {'a', 'e', 'i', 'l', 'o', 'u', 'y'},
    'm': {'a', 'e', 'i', 'n', 'o', 'u', 'y'},
    'n': {'a', 'e', 'i', 'o', 'u', 'y'},
    'o': {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
          'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z'},
    'p': {'a', 'e', 'h', 'i', 'l', 'n', 'o', 'r',
          's', 't', 'u', 'y'},
    'q': {'u'},
    'r': {'a', 'e', 'h', 'i', 'o', 'u', 'y'},
    's': {'a', 'c', 'e', 'h', 'i', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 't', 'u', 'w', 'y'},
    't': {'a', 'e', 'h', 'i', 'o', 'r', 's', 'u',
          'w', 'y'},
    'u': {'b', 'd', 'g', 'k', 'l', 'm', 'n', 'p',
          'r', 's', 't'},
    'v': {'a', 'e', 'i', 'o', 'u', 'y'},
    'w': {'a', 'e', 'h', 'i', 'o', 'r', 'u'},
    'x': {'e', 'y'},
    'y': {'a', 'e', 'i', 'o', 'u'},
    'z': {'a', 'e', 'i', 'o', 'y'}}

memoized_partitions = {0: 1}
memoized_sum_of_factors = dict()
memoized_primeness = {1: False,
                      2: True}
memoized_prime_numbers = [2, 3, 5]
memoized_spiral_corners = dict()
memoized_sqrt_continued_fractions_periods = dict()

multiply = partial(reduce, operator.mul)


def capacity(iterable: Iterable[Any]) -> int:
    return sum(1 for _ in iterable)


def star_filter(function: Callable[..., bool],
                iterable: Iterable) -> Iterator[Any]:
    yield from (element
                for element in iterable
                if function(*element))


def map_tuples(elements: Iterable[Any],
               *,
               function: Callable[[Any], Any]
               ) -> Iterable[Tuple[Any, Any]]:
    for number in elements:
        yield function(number), number


def collect_mapping(keys_values: Iterable[Tuple[Hashable, Any]],
                    mapping_type: Callable[[], MutableMapping] = dict,
                    values_container: Callable[[], MutableSequence] = list
                    ) -> MutableMapping:
    dictionary = mapping_type()
    for key, value in keys_values:
        dictionary.setdefault(key, values_container()).append(value)
    return dictionary


def has_n_elements(collection: Collection[Any],
                   *,
                   n: int) -> bool:
    return len(collection) == n


def chunks(sequence: Sequence[Any],
           size: int,
           *,
           exact: bool = False) -> Iterable[Sequence[Any]]:
    elements_count = len(sequence)
    stop = elements_count - size + 1 if exact else elements_count
    for offset in range(stop):
        yield sequence[offset:offset + size]


def sort_permutation(permutation: Sequence[int]) -> Sequence[int]:
    min_index, _ = min(enumerate(permutation),
                       key=operator.itemgetter(1))
    return rotate(permutation, min_index)


def rotate(sequence: Sequence[Any],
           position: int) -> Sequence[Any]:
    return sequence[position:] + sequence[:position]


def bisect(sequence: Sequence[Any]) -> Tuple[Sequence[Any],
                                             Sequence[Any]]:
    middle = len(sequence) // 2
    return sequence[:middle], sequence[middle:]


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


def parse_lines(lines: Iterable[str],
                *,
                sep: str = ',',
                strip_chars: str = '"') -> Iterable[str]:
    for line in lines:
        yield from (word.strip(strip_chars)
                    for word in line.split(sep))


def max_number(digits_count: int) -> int:
    return 10 ** digits_count - 1


def number_digits_sum(number: int) -> int:
    return sum(number_to_digits(number))


def number_digits_count(number: int) -> int:
    return len(str(number))


def number_to_digits(number: int) -> Iterable[int]:
    yield from map(int, str(number))


def digits_to_number(digits: Iterable[int]) -> int:
    return int(''.join(map(str, digits)))


def phi(number: int) -> Fraction:
    return number / n_phi(number)


def n_phi(number: int) -> Fraction:
    print(number)
    # based on
    # https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler.27s_product_formula
    prime_factors = filter(prime, factors(number))
    numerators, denominators = zip(*((factor, factor - 1)
                                     for factor in prime_factors))
    return Fraction(multiply(numerators),
                    multiply(denominators))


def sum_of_factors(number: int) -> int:
    try:
        return memoized_sum_of_factors[number]
    except KeyError:
        result = sum(factors(number))
        memoized_sum_of_factors[number] = result
        return result


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


def factors(number: int,
            *,
            start: int = 1) -> Set[int]:
    candidates = range(start, int_sqrt(number) + 1)
    return {1} | set(chain.from_iterable((candidate, number // candidate)
                                         for candidate in candidates
                                         if number % candidate == 0))


proper_divisors = partial(factors,
                          start=2)


def fibonacci_numbers(stop: Real = float('inf')) -> Iterable[int]:
    a, b = 0, 1
    while b < stop:
        yield b
        a, b = b, a + b


def prime_numbers(stop: int,
                  *,
                  reverse: bool = False) -> Iterator[int]:
    global memoized_prime_numbers
    max_memoized_prime_number = memoized_prime_numbers[-1]
    if stop < max_memoized_prime_number:
        stop_indices = (
            len(memoized_prime_numbers) - index
            for (index,
                 prime_number) in enumerate(reversed(memoized_prime_numbers))
            if prime_number < stop)
        stop_index = next(stop_indices, 0)
        result = memoized_prime_numbers[:stop_index]
        if reverse:
            result = reversed(result)
        yield from result
        return
    # based on
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    # TODO: refactor this mess
    initial_primes = [2, 3]
    initial_primes = filter(partial(operator.gt, stop),
                            initial_primes)
    if reverse:
        initial_primes = reversed(list(initial_primes))
    else:
        yield from initial_primes

    stop_mod_six = stop % 6
    correction = stop_mod_six > 1
    stop = {0: stop,
            1: stop - 1,
            2: stop + 4,
            3: stop + 3,
            4: stop + 2,
            5: stop + 1}[stop_mod_six]
    sieve = primes_sieve(stop)

    indices = range(1, stop // 3 - correction)
    if reverse:
        indices = reversed(indices)
    prime_numbers_list = []
    for index in indices:
        candidate = 3 * index + 1 | 1
        if sieve[index]:
            prime_numbers_list.append(candidate)
            memoized_primeness[candidate] = True
            yield candidate
        else:
            memoized_primeness[candidate] = False
    memoized_prime_numbers = sorted(set(memoized_prime_numbers
                                        + prime_numbers_list))
    yield from initial_primes


def primes_sieve(stop: int) -> List[bool]:
    sieve = [True] * (stop // 3)
    sieve[0] = False
    factor_stop = int_sqrt(stop) // 3 + 1
    for factor in range(factor_stop):
        if not sieve[factor]:
            continue

        k = 3 * factor + 1 | 1
        k_squared = k ** 2
        k_doubled = 2 * k
        number_sixth_part_pred = stop // 6 - 1
        sieve[(k_squared // 3)::k_doubled] = (
            [False]
            * ((number_sixth_part_pred - k_squared // 6) // k + 1))

        k_diff = k_squared + 4 * k - k_doubled * (factor & 1)
        sieve[k_diff // 3::k_doubled] = (
            [False]
            * ((number_sixth_part_pred - k_diff // 6) // k + 1))
    return sieve


def reduced_proper_fractions(*,
                             start: Fraction = Fraction(0, 1),
                             stop: Fraction,
                             max_denominator: int,
                             only_first: bool = False) -> Iterable[Fraction]:
    start_numerator, start_denominator = start.numerator, start.denominator
    stop_numerator, stop_denominator = stop.numerator, stop.denominator
    stop_float = float(stop)
    for denominator in range(max_denominator, 1, -1):
        for numerator in range(int(stop_float * denominator), 0, -1):
            if start_numerator * denominator >= start_denominator * numerator:
                continue
            if stop_denominator * numerator >= stop_numerator * denominator:
                continue
            if not relatively_prime(numerator, denominator):
                continue
            yield Fraction(numerator, denominator)
            if only_first:
                break


def prime(number: int) -> bool:
    try:
        return memoized_primeness[number]
    except KeyError:
        if not odd(number):
            result = False
            memoized_primeness[number] = result
            return result
        factors_candidates = prime_numbers(int_sqrt(number) + 1)
        for candidate in factors_candidates:
            if number % candidate == 0:
                result = False
                break
        else:
            result = True
        memoized_primeness[number] = result
        return result


def odd(number: int) -> int:
    return number & 1


def relatively_prime(number: int, other_number: int) -> bool:
    return gcd(number, other_number) == 1


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def integer_right_triangles(max_perimeter: int
                            ) -> Iterable[Tuple[int, int, int]]:
    def is_perimeter_valid(triplet: Tuple[int, int, int]) -> bool:
        return sum(triplet) <= max_perimeter

    yield from filter(is_perimeter_valid,
                      pythagorean_triplets(max_perimeter))


def pythagorean_triplets(stop: int) -> Iterable[int]:
    yield from set(filter(is_pythagorean_triplet,
                          pythagorean_triplets_candidates(stop)))


def is_pythagorean_triplet(triplet: Tuple[int, int, int]) -> bool:
    a, b, c = triplet
    return a ** 2 + b ** 2 == c ** 2


def pythagorean_triplets_candidates(stop: int
                                    ) -> Iterable[Tuple[int, int, int]]:
    # based on
    # https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    min_n = 1
    min_m = 2
    max_k = stop // (min_n ** 2 + min_m ** 2)
    for k in range(1, max_k + 1):
        numbers = range(1, int_sqrt(stop // k))
        for n, m in map(sorted, permutations(numbers,
                                             r=2)):
            candidate = sorted([m ** 2 - n ** 2,
                                2 * m * n,
                                m ** 2 + n ** 2])
            yield tuple(k * coordinate
                        for coordinate in candidate)


def polygonal(number: int,
              *,
              dimension: int) -> bool:
    """
    Polygonal numbers has form:
        number = [(dimension - 2) * index ** 2 - (dimension - 4) * index] / 2

    from
    https://en.wikipedia.org/wiki/Polygonal_number
    """
    a = dimension - 2
    minus_b = dimension - 4
    minus_c = 2 * number
    discriminant = minus_b ** 2 + 4 * a * minus_c
    return (is_perfect_square(discriminant) and
            (minus_b + int_sqrt(discriminant)) % (2 * a) == 0)


triangular = partial(polygonal,
                     dimension=3)

pentagonal = partial(polygonal,
                     dimension=5)


def is_perfect_square(number: int) -> bool:
    try:
        return sqrt(number).is_integer()
    except ValueError:
        return False


def int_sqrt(number: int) -> int:
    return int(sqrt(number))


def binomial_coefficient(n: int, k: int) -> int:
    numerators = range(n - k + 1, n + 1)
    return multiply(numerators) // factorial(k)


def spiral_corners(dimension: int,
                   *,
                   start: int = SPIRAL_START
                   ) -> Iterable[Tuple]:
    for dimension in range(3, dimension + 2, 2):
        try:
            yield memoized_spiral_corners[dimension]
        except KeyError:
            decrement = dimension - 1
            right_top = dimension * dimension + start - 1
            left_top = right_top - decrement
            left_bottom = left_top - decrement
            right_bottom = left_bottom - decrement
            corners = right_bottom, left_bottom, left_top, right_top
            memoized_spiral_corners[dimension] = corners
            yield corners


def english_text(text: str,
                 *,
                 acceptable_non_english_words_ratio: float = 0.1
                 ) -> bool:
    word_index = 0
    non_english_words_count = 0
    for word_index, word in enumerate(map(str.lower, words(text)),
                                      start=1):
        try:
            first_letter, second_letter, *_ = word
            if second_letter not in FIRST_LETTERS_FOLLOWERS[first_letter]:
                non_english_words_count += 1
        except ValueError:
            # single-letter word
            continue
    try:
        # in the end word index corresponds to words count
        non_english_words_ratio = non_english_words_count / word_index
    except ZeroDivisionError:
        return False
    else:
        return non_english_words_ratio <= acceptable_non_english_words_ratio


def words(text: str) -> Iterable[str]:
    yield from filter(str.isalpha,
                      (word.group(0)
                       for word in WORDS_RE.finditer(text)))


def sqrt_continued_fraction(number: int) -> Iterable[int]:
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


def sqrt_continued_fraction_period(number: int,
                                   *,
                                   members_count_start: int = 250,
                                   members_count_step: int = 50,
                                   precision_start: int = 500,
                                   precision_step: int = 250,
                                   precision_stop: int = 2_501
                                   ) -> Sequence[int]:
    try:
        return memoized_sqrt_continued_fractions_periods[number]
    except KeyError:
        for members_count in count(members_count_start,
                                   members_count_step):
            for precision in range(precision_start,
                                   precision_stop,
                                   precision_step):
                context = Context(prec=precision)
                setcontext(context)
                sequence = list(islice(sqrt_continued_fraction(number),
                                       1,
                                       members_count))
                cycle = find_cycle(sequence)
                if cycle is not None:
                    memoized_sqrt_continued_fractions_periods[number] = cycle
                    return cycle


def sqrt_convergent(number: int,
                    index: int,
                    *,
                    members_count_start: int = 250,
                    members_count_step: int = 50,
                    precision_start: int = 500,
                    precision_step: int = 250,
                    precision_stop: int = 2_501
                    ):
    period = sqrt_continued_fraction_period(
        number,
        members_count_start=members_count_start,
        members_count_step=members_count_step,
        precision_start=precision_start,
        precision_step=precision_step,
        precision_stop=precision_stop)
    first_coefficient = Fraction(int_sqrt(number))
    coefficients = list(islice(chain.from_iterable(repeat(period)), index))
    try:
        increment = coefficients.pop()
    except IndexError:
        return first_coefficient
    for coefficient in reversed(coefficients):
        increment = coefficient + Fraction(1, increment)
    return first_coefficient + Fraction(1, increment)


def aggregated_path_sum(*,
                        rows: Iterable[Iterable[int]],
                        successors_count: int,
                        function: Callable[[Iterable[int]], int]) -> int:
    rows_reversed = reversed(rows)
    next_row = next(rows_reversed)
    for row in rows_reversed:
        next_row = tuple(number
                         + function(next_row[index:index + successors_count])
                         for index, number in enumerate(row))
    result, = next_row
    return result


maximum_path_sum = partial(aggregated_path_sum,
                           function=max)
minimum_path_sum = partial(aggregated_path_sum,
                           function=min)
