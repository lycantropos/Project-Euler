from itertools import product
from typing import (Any,
                    Union,
                    Iterable,
                    Iterator,
                    Dict,
                    Tuple,
                    Set,
                    List)

from utils import (prime_numbers,
                   number_digits_count,
                   collect_mapping,
                   star_filter)


def primes_chains(stop: int) -> Iterable[List[int]]:
    primes_pairs_dict = collect_mapping(primes_pairs(stop))
    parents, children = zip(*primes_pairs_dict.items())
    primes_pairs_dict = dict(zip(parents, map(set, children)))

    for number, pairs in sorted(primes_pairs_dict.items()):
        for tree in trees(chain=pairs,
                          links=primes_pairs_dict):
            yield from chains(tree,
                              links=[number])


def trees(chain: Set[Any],
          links: Dict[Any, Set[Any]]
          ) -> Iterable[Tuple[int, List[int]]]:
    for link in chain:
        linkage = chain & links[link]
        if linkage:
            yield link, list(trees(linkage,
                                   links))
    yield from chain


def chains(tree: Union[int, Iterable[Tuple[int, List[int]]]],
           links: List[int]) -> Iterable[List[int]]:
    try:
        link, rest = tree
    except TypeError:
        yield links + [tree]
    else:
        for sub_chain in rest:
            yield from chains(sub_chain,
                              links=links + [link])


def primes_pairs(stop: int) -> Iterable[Tuple[int, int]]:
    prime_numbers_generator = prime_numbers(stop)

    # we're skipping 2
    # because right concatenation with it
    # will always give even (hence non-prime) number
    prime_numbers_set = set(prime_numbers_generator)
    numbers_by_digits_count = collect_mapping(
        digits_counts_numbers(prime_numbers_set))

    def primes_paired(prime_number: int,
                      other_prime_number: int) -> bool:
        left_concatenation = int(str(prime_number) + str(other_prime_number))
        right_concatenation = int(str(other_prime_number) + str(prime_number))
        return (left_concatenation in prime_numbers_set and
                right_concatenation in prime_numbers_set)

    max_digits_count = number_digits_count(max(prime_numbers_set))
    for digits_count in range(1, max_digits_count // 2 + 1):
        numbers = numbers_by_digits_count[digits_count]
        max_candidates_digits_count = max_digits_count - digits_count + 1
        for candidates_digits_count in range(digits_count,
                                             max_candidates_digits_count):
            candidates = numbers_by_digits_count[candidates_digits_count]
            pairs = list(star_filter(primes_paired,
                                     product(numbers, candidates)))
            for pair in pairs:
                yield pair
                # pairing relation is symmetric
                yield reversed(pair)


def digits_counts_numbers(numbers: Iterable[int]
                          ) -> Iterable[Tuple[int, int]]:
    for number in numbers:
        yield number_digits_count(number), number


def prime_pair_sets(*,
                    stop: int,
                    target_chain_length: int) -> Iterator[List[int]]:
    for chain in primes_chains(stop):
        if len(chain) >= target_chain_length:
            yield chain


first_four_elements_primes_chain = next(prime_pair_sets(stop=1_000_000,
                                                        target_chain_length=4))
first_five_elements_primes_chain = next(prime_pair_sets(stop=100_000_000,
                                                        target_chain_length=5))

assert set(first_four_elements_primes_chain) == {3, 7, 109, 673}
assert set(first_five_elements_primes_chain) == {13, 5701, 5197, 6733, 8389}
assert sum(first_five_elements_primes_chain) == 26_033
