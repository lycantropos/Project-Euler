import operator
from collections import Counter
from functools import partial
from itertools import (product,
                       chain,
                       combinations,
                       filterfalse,
                       starmap)
from typing import (Iterable,
                    Tuple,
                    Set)

from utils import chunks

LOWEST_STRAIGHTS_ACE_RANK = -1

HAND_SIZE = 5

HandType = Set[str]
HIGHER_RANKS = ['T', 'J', 'Q', 'K', 'A']
ACE = 'A'
LOWER_RANKS = list(map(str, range(2, 10)))
RANKS = LOWER_RANKS + HIGHER_RANKS
SUITS = {'D', 'H', 'S', 'C'}


def other_ranks(*ranks: str) -> Iterable[str]:
    yield from filterfalse(partial(operator.contains,
                                   ranks), RANKS)


def cards(*ignored_ranks: str,
          count: int,
          cards_suits: Iterable[Iterable[str]]):
    ranks = other_ranks(*ignored_ranks) if ignored_ranks else RANKS
    for ranks in combinations(ranks,
                              r=count):
        for suits in cards_suits:
            yield tuple(rank + suit for rank, suit in zip(ranks, suits))


def cards_of_a_kind(rank: str,
                    *,
                    count: int) -> Iterable[Tuple[str]]:
    for suits in combinations(SUITS,
                              r=count):
        yield tuple(rank + suit for suit in suits)


pairs = partial(cards_of_a_kind,
                count=2)
triplets = partial(cards_of_a_kind,
                   count=3)

ROYAL_FLUSHES = {frozenset(rank + suit for rank in HIGHER_RANKS)
                 for suit in SUITS}
STRAIGHT_FLUSHES = ({frozenset(rank + suit
                               for rank in ranks)
                     for suit in SUITS
                     for ranks in chunks(RANKS, HAND_SIZE,
                                         exact=True)}
                    | {frozenset(rank + suit
                                 for rank in ([ACE] + LOWER_RANKS)[:HAND_SIZE])
                       for suit in SUITS})
FOURS_OF_A_KIND = set(chain.from_iterable(map(frozenset,
                                              cards_of_a_kind(rank,
                                                              count=4))
                                          for rank in RANKS))
FULL_HOUSES = {frozenset(pair + triplet)
               for rank in RANKS
               for other_rank in other_ranks(rank)
               for pair in pairs(rank)
               for triplet in triplets(other_rank)}
FLUSHES = {frozenset(hand)
           for hand in cards(count=HAND_SIZE,
                             cards_suits=[(suit,) * HAND_SIZE
                                          for suit in SUITS])}
STRAIGHTS = ({frozenset(rank + suit
                        for rank, suit in zip(ranks, suits))
              for suits in product(SUITS, repeat=HAND_SIZE)
              for ranks in chunks(RANKS, HAND_SIZE,
                                  exact=True)}
             | {frozenset(rank + suit
                          for (rank,
                               suit) in zip((['A'] + LOWER_RANKS)[:HAND_SIZE],
                                            suits))
                for suits in product(SUITS, repeat=HAND_SIZE)})
THREES_OF_A_KIND = set(chain.from_iterable(map(frozenset,
                                               cards_of_a_kind(rank,
                                                               count=3))
                                           for rank in RANKS))
TWO_PAIRS = {frozenset(first_pair + second_pair)
             for first_rank in RANKS
             for second_rank in other_ranks(first_rank)
             for first_pair in pairs(first_rank)
             for second_pair in pairs(second_rank)}
PAIRS = set(chain.from_iterable(map(frozenset,
                                    cards_of_a_kind(rank,
                                                    count=2))
                                for rank in RANKS))
COMBINATIONS = [ROYAL_FLUSHES,
                STRAIGHT_FLUSHES,
                FOURS_OF_A_KIND,
                FULL_HOUSES,
                FLUSHES,
                STRAIGHTS,
                THREES_OF_A_KIND,
                TWO_PAIRS,
                PAIRS]


def games_results(hands: Iterable[Tuple[HandType, HandType]]
                  ) -> Iterable[bool]:
    yield from starmap(first_player_wins, hands)


def parse_hands(lines: Iterable[str]
                ) -> Iterable[Tuple[HandType, HandType]]:
    for line in lines:
        players_cards = line.rstrip().split(' ')
        yield (frozenset(players_cards[:HAND_SIZE]),
               frozenset(players_cards[HAND_SIZE:]))


def hand_strength(hand: HandType) -> Tuple[int, ...]:
    for index, hands_combinations in enumerate(COMBINATIONS):
        try:
            combination = next(combination
                               for combination in hands_combinations
                               if not combination - hand)
        except StopIteration:
            continue
        other_cards = hand - combination
        return (len(COMBINATIONS) - index - 1,
                *hand_ranks_strength(combination),
                *hand_ranks_strength(other_cards))
    return (-1, *hand_ranks_strength(hand))


def hand_ranks_strength(hand: HandType) -> Tuple[int, ...]:
    ranks = list(hand_ranks(hand))
    if hand in STRAIGHTS and ACE in ranks:
        non_ace_ranks = list(filter(partial(operator.eq,
                                            ACE),
                                    ranks))
        if all(rank in LOWER_RANKS
               for rank in non_ace_ranks):
            return (*sorted(map(RANKS.index, non_ace_ranks),
                            reverse=True),
                    LOWEST_STRAIGHTS_ACE_RANK)
    if hand in FULL_HOUSES:
        ranks_counter = Counter(ranks)
        return tuple(RANKS.index(rank)
                     for rank, count in ranks_counter.most_common(2)
                     for _ in range(count))
    return tuple(sorted(map(RANKS.index, ranks),
                        reverse=True))


def hand_ranks(hand: HandType) -> Iterable[str]:
    for rank, _ in hand:
        yield rank


def first_player_wins(first_player_hand: HandType,
                      second_player_hand: HandType
                      ) -> bool:
    return (hand_strength(first_player_hand)
            > hand_strength(second_player_hand))


with open('poker.txt', mode='r') as poker_hands_file:
    hands = list(parse_hands(poker_hands_file))

assert not first_player_wins({'5H', '5C', '6S', '7S', 'KD'},
                             {'2C', '3S', '8S', '8D', 'TD'})
assert first_player_wins({'5D', '8C', '9S', 'JS', 'AC'},
                         {'2C', '5C', '7D', '8S', 'QH'})
assert not first_player_wins({'2D', '9C', 'AS', 'AH', 'AC'},
                             {'3D', '6D', '7D', 'TD', 'QD'})
assert first_player_wins({'4D', '6S', '9H', 'QH', 'QC'},
                         {'3D', '6D', '7H', 'QD', 'QS'})
assert first_player_wins({'2H', '2D', '4C', '4D', '4S'},
                         {'3C', '3D', '3S', '9S', '9D'})
assert sum(games_results(hands)) == 376
